"""starlette-html is a Python-first HTML DSL for Starlette apps.

It lets you build server-rendered HTML with plain Python functions:

- HTML tags are Python callables
- components are ordinary Python functions
- children are positional arguments
- attributes are keyword arguments
- rendering escapes dynamic content by default

Import from this package for the core DSL, rendering helpers, and thin
Starlette response helpers.
"""

from starlette_html.core import (
    Fragment,
    Markup,
    a,
    body,
    button,
    create_element,
    div,
    h1,
    h2,
    head,
    html,
    input_,
    li,
    meta,
    p,
    render,
    render_document,
    script,
    span,
    title,
    ul,
)
from starlette_html.starlette import HTML, Document

__all__ = [
    "HTML",
    "Document",
    "Fragment",
    "Markup",
    "a",
    "body",
    "button",
    "create_element",
    "div",
    "h1",
    "h2",
    "head",
    "html",
    "input_",
    "li",
    "meta",
    "p",
    "render",
    "render_document",
    "script",
    "span",
    "title",
    "ul",
]
