"""Core HTML node and rendering primitives for starlette-html."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape

VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


@dataclass(slots=True)
class Element:
    """A rendered HTML element node."""

    tag: str
    attrs: dict[str, object]
    children: tuple[object, ...]


class Fragment:
    """A group of sibling nodes rendered without a wrapper tag."""

    __slots__ = ("children",)

    def __init__(self, *children: object) -> None:
        """Create a fragment from the provided children."""
        self.children = children


class Markup(str):
    """Explicitly trusted HTML."""

    __slots__ = ()


def _normalize_attr_name(name: str) -> str:
    if name == "cls":
        return "class"
    if name == "for_":
        return "for"
    if name.endswith("_"):
        name = name.removesuffix("_")
    return name.replace("_", "-")


def _render_attr_name(name: str) -> str:
    normalized = _normalize_attr_name(name)
    if normalized.startswith("on"):
        msg = f"event handler attributes are blocked in v0.1: {name!r}"
        raise ValueError(msg)
    return normalized


def _flatten_children(children: tuple[object, ...]) -> tuple[object, ...]:
    flattened: list[object] = []
    for child in children:
        if child is None or child is False:
            continue
        if isinstance(child, (list, tuple)):
            flattened.extend(_flatten_children(tuple(child)))
            continue
        flattened.append(child)
    return tuple(flattened)


def create_element(tag: str, *children: object, **attrs: object) -> Element:
    """Create an element node."""
    return Element(tag=tag, attrs=attrs, children=_flatten_children(children))


def _render_children(children: tuple[object, ...]) -> str:
    return "".join(_render_node(child) for child in children)


def _render_attrs(attrs: dict[str, object]) -> str:
    rendered: list[str] = []
    for raw_name, value in attrs.items():
        name = _render_attr_name(raw_name)
        if value is None or value is False:
            continue
        if value is True:
            rendered.append(f" {name}")
            continue
        rendered.append(f' {name}="{escape(str(value), quote=True)}"')
    return "".join(rendered)


def _render_node(node: object) -> str:
    rendered = ""
    if node is None or node is False:
        rendered = ""
    elif isinstance(node, Markup):
        rendered = str(node)
    elif isinstance(node, Fragment):
        rendered = _render_children(node.children)
    elif isinstance(node, Element):
        attrs = _render_attrs(node.attrs)
        if node.tag in VOID_TAGS:
            if node.children:
                msg = f"void element {node.tag!r} cannot have children"
                raise ValueError(msg)
            rendered = f"<{node.tag}{attrs} />"
        else:
            children = _render_children(node.children)
            rendered = f"<{node.tag}{attrs}>{children}</{node.tag}>"
    elif isinstance(node, bool):
        rendered = "True"
    elif isinstance(node, (str, int, float)):
        rendered = escape(str(node))
    elif isinstance(node, (list, tuple)):
        rendered = _render_children(tuple(node))
    else:
        rendered = escape(str(node))
    return rendered


def render(node: object) -> str:
    """Render a node tree or text node into an HTML fragment."""
    return _render_node(node)


def render_document(node: object) -> str:
    """Render a complete HTML document with a doctype."""
    return f"<!doctype html>{render(node)}"
