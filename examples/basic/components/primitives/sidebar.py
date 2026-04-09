"""Generic sidebar primitives for the basic example.

These primitives model the sidebar as a set of low-level building blocks rather
than a data-driven app component. They are meant to be composed together to
build app-specific sidebars such as `AppSidebar`.

Use these primitives when you want:

- a generic sidebar container that accepts arbitrary children
- reusable sidebar sub-structures such as header, content, footer, and menus
- styling hooks through stable CSS classes
- a place to attach future behavior hooks such as collapsible state or triggers

The intended usage style is composition-first. For example:

```python
Sidebar(
    SidebarHeader(...),
    SidebarContent(
        SidebarGroup(
            SidebarGroupLabel("Platform"),
            SidebarMenu(
                SidebarMenuItem(
                    SidebarMenuButton(
                        "Playground",
                        render_as=a(href="/playground"),
                    )
                )
            ),
        )
    ),
    SidebarFooter(...),
)
```

Customization happens by composing different children and, when needed, passing
additional `cls` values into each primitive. These primitives should stay
generic and should not know about application-specific concepts like brands,
teams, projects, or users.
"""

from typing import TYPE_CHECKING

from starlette_html import render_as as apply_render_as
from starlette_html.tags import (
    aside,
    div,
    header,
    li,
    main,
    nav,
    p,
    section,
    span,
    style,
    ul,
)

if TYPE_CHECKING:
    from starlette_html.core import Element


def SidebarRoot(*children: object, **attrs: object) -> object:
    """Render the outer sidebar element."""
    return aside(*children, cls=["sidebar", attrs.pop("cls", None)], **attrs)


def Sidebar(*children: object, **attrs: object) -> object:
    """Render a generic sidebar container."""
    return SidebarRoot(*children, **attrs)


def SidebarHeader(*children: object, **attrs: object) -> object:
    """Render the sidebar header region."""
    return header(*children, cls=["sidebar__header", attrs.pop("cls", None)], **attrs)


def SidebarContent(*children: object, **attrs: object) -> object:
    """Render the scrollable sidebar content region."""
    return nav(*children, cls=["sidebar__nav", attrs.pop("cls", None)], **attrs)


def SidebarFooter(*children: object, **attrs: object) -> object:
    """Render the sidebar footer region."""
    return div(*children, cls=["sidebar__footer", attrs.pop("cls", None)], **attrs)


def SidebarGroup(*children: object, **attrs: object) -> object:
    """Render a sidebar section/group."""
    return section(*children, cls=["sidebar__section", attrs.pop("cls", None)], **attrs)


def SidebarGroupLabel(*children: object, **attrs: object) -> object:
    """Render a sidebar group label."""
    return p(
        *children,
        cls=["sidebar__section-title", attrs.pop("cls", None)],
        **attrs,
    )


def SidebarGroupAction(
    *children: object,
    render_as: Element | None = None,
    **attrs: object,
) -> object:
    """Render an action attached to a sidebar group header."""
    resolved_attrs = {
        "cls": ["sidebar__group-action", attrs.pop("cls", None)],
        **attrs,
    }
    if render_as is None:
        resolved_attrs["type"] = "button"

    return apply_render_as(
        render_as,
        default_tag="button",
        children=children,
        attrs=resolved_attrs,
    )


def SidebarGroupContent(*children: object, **attrs: object) -> object:
    """Render the main content container for a sidebar group."""
    return div(
        *children,
        cls=["sidebar__group-content", attrs.pop("cls", None)],
        **attrs,
    )


def SidebarMenu(*children: object, **attrs: object) -> object:
    """Render a sidebar menu list."""
    return ul(*children, cls=["sidebar__items", attrs.pop("cls", None)], **attrs)


def SidebarMenuItem(*children: object, **attrs: object) -> object:
    """Render a sidebar menu item container."""
    return li(*children, cls=["sidebar__item", attrs.pop("cls", None)], **attrs)


def SidebarMenuButton(
    *children: object,
    active: bool = False,
    render_as: Element | None = None,
    **attrs: object,
) -> object:
    """Render a primary sidebar navigation button."""
    resolved_attrs = {
        "cls": ["sidebar__item-link", attrs.pop("cls", None)],
        "data_active": str(active).lower(),
        "aria_current": "page" if active else None,
        **attrs,
    }
    if render_as is None:
        resolved_attrs["type"] = "button"

    return apply_render_as(
        render_as,
        default_tag="button",
        children=children,
        attrs=resolved_attrs,
    )


def SidebarMenuAction(
    *children: object,
    render_as: Element | None = None,
    **attrs: object,
) -> object:
    """Render an action aligned to a sidebar menu item."""
    resolved_attrs = {
        "cls": ["sidebar__menu-action", attrs.pop("cls", None)],
        **attrs,
    }
    if render_as is None:
        resolved_attrs["type"] = "button"

    return apply_render_as(
        render_as,
        default_tag="button",
        children=children,
        attrs=resolved_attrs,
    )


def SidebarMenuBadge(*children: object, **attrs: object) -> object:
    """Render a badge within a sidebar menu item."""
    return span(
        *children,
        cls=["sidebar__item-badge", attrs.pop("cls", None)],
        **attrs,
    )


def SidebarMenuSub(*children: object, **attrs: object) -> object:
    """Render a nested sidebar menu list."""
    return ul(
        *children,
        cls=["sidebar__item-children", attrs.pop("cls", None)],
        **attrs,
    )


def SidebarMenuSubItem(*children: object, **attrs: object) -> object:
    """Render a nested sidebar menu item container."""
    return li(
        *children,
        cls=["sidebar__sub-item", attrs.pop("cls", None)],
        **attrs,
    )


def SidebarMenuSubButton(
    *children: object,
    active: bool = False,
    render_as: Element | None = None,
    **attrs: object,
) -> object:
    """Render a nested sidebar navigation button."""
    resolved_attrs = {
        "data_active": str(active).lower(),
        "aria_current": "page" if active else None,
        **attrs,
    }
    if render_as is None:
        resolved_attrs["type"] = "button"

    return apply_render_as(
        render_as,
        default_tag="button",
        children=children,
        attrs=resolved_attrs,
    )


def SidebarRail(*children: object, **attrs: object) -> object:
    """Render a thin rail placeholder for future collapsed-sidebar affordances."""
    return div(*children, cls=["sidebar__rail", attrs.pop("cls", None)], **attrs)


def SidebarInset(*children: object, **attrs: object) -> object:
    """Render the main content area that sits beside the sidebar."""
    return main(*children, cls=["sidebar__inset", attrs.pop("cls", None)], **attrs)


def SidebarTrigger(
    *children: object,
    render_as: Element | None = None,
    **attrs: object,
) -> object:
    """Render a trigger for future sidebar open and close behavior."""
    resolved_attrs = {
        "cls": ["sidebar__trigger", attrs.pop("cls", None)],
        "aria_label": attrs.pop("aria_label", "Toggle sidebar"),
        **attrs,
    }
    if render_as is None:
        resolved_attrs["type"] = "button"

    trigger_children = children or ("Toggle",)
    return apply_render_as(
        render_as,
        default_tag="button",
        children=trigger_children,
        attrs=resolved_attrs,
    )


def SidebarStyles() -> object:
    """Shared styles for the sidebar demo."""
    return style(
        """
        :root {
          color-scheme: light;
          --page-bg: #f8fafc;
          --panel-bg: #ffffff;
          --panel-border: #e2e8f0;
          --panel-muted: #64748b;
          --panel-text: #0f172a;
          --panel-soft: #f1f5f9;
          --panel-accent: #e0e7ff;
          --panel-accent-text: #312e81;
          --content-accent: #eef2ff;
          --shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
        }

        * {
          box-sizing: border-box;
        }

        body {
          margin: 0;
          font-family: Inter, ui-sans-serif, system-ui, -apple-system,
            BlinkMacSystemFont, "Segoe UI", sans-serif;
          background: var(--page-bg);
          color: var(--panel-text);
        }

        a {
          color: inherit;
          text-decoration: none;
        }

        .app-shell {
          min-height: 100vh;
          display: grid;
          grid-template-columns: 18rem minmax(0, 1fr);
        }

        .sidebar {
          display: flex;
          flex-direction: column;
          gap: 1.5rem;
          padding: 1.5rem 1rem;
          border-right: 1px solid var(--panel-border);
          background: var(--panel-bg);
        }

        .sidebar__header,
        .sidebar__footer {
          padding: 0 0.5rem;
        }

        .sidebar__brand {
          display: flex;
          align-items: center;
          gap: 0.875rem;
        }

        .sidebar__brand-mark,
        .sidebar__item-icon,
        .sidebar__user-avatar {
          width: 2.25rem;
          height: 2.25rem;
          border-radius: 0.8rem;
          display: inline-flex;
          align-items: center;
          justify-content: center;
          flex: none;
          font-size: 0.875rem;
          font-weight: 700;
          background: var(--panel-soft);
        }

        .sidebar__brand-mark {
          background: linear-gradient(135deg, #4f46e5, #7c3aed);
          color: #ffffff;
        }

        .sidebar__eyebrow,
        .sidebar__section-title,
        .sidebar__user-email,
        .sidebar__item-children a {
          color: var(--panel-muted);
        }

        .sidebar__title,
        .sidebar__user-name {
          margin: 0;
          font-size: 0.95rem;
          font-weight: 700;
        }

        .sidebar__eyebrow,
        .sidebar__user-email,
        .sidebar__item-children a {
          font-size: 0.85rem;
        }

        .sidebar__nav {
          display: flex;
          flex-direction: column;
          gap: 1.25rem;
        }

        .sidebar__section {
          display: flex;
          flex-direction: column;
          gap: 0.5rem;
        }

        .sidebar__group-content {
          display: flex;
          flex-direction: column;
          gap: 0.5rem;
        }

        .sidebar__section-title {
          padding: 0 0.75rem;
          text-transform: uppercase;
          letter-spacing: 0.08em;
          font-size: 0.72rem;
          font-weight: 700;
        }

        .sidebar__items,
        .sidebar__item-children {
          list-style: none;
          margin: 0;
          padding: 0;
        }

        .sidebar__item {
          display: flex;
          flex-direction: column;
          gap: 0.4rem;
        }

        .sidebar__sub-item {
          list-style: none;
        }

        .sidebar__item-link {
          display: flex;
          align-items: center;
          gap: 0.75rem;
          width: 100%;
          border: 0;
          background: none;
          min-height: 3rem;
          padding: 0.65rem 0.75rem;
          border-radius: 1rem;
          font: inherit;
          text-align: left;
          color: var(--panel-text);
          cursor: pointer;
        }

        .sidebar__item-link:hover {
          background: var(--panel-soft);
        }

        .sidebar__item-link[data-active="true"] {
          background: var(--panel-accent);
          color: var(--panel-accent-text);
        }

        .sidebar__item-label {
          flex: 1;
          font-weight: 600;
        }

        .sidebar__item-badge {
          border-radius: 999px;
          padding: 0.15rem 0.5rem;
          font-size: 0.72rem;
          font-weight: 700;
          background: rgba(79, 70, 229, 0.12);
        }

        .sidebar__group-action,
        .sidebar__menu-action,
        .sidebar__trigger {
          border: 0;
          background: none;
          font: inherit;
          color: inherit;
          cursor: pointer;
        }

        .sidebar__menu-action {
          align-self: flex-end;
          padding: 0.25rem 0.4rem;
          border-radius: 0.6rem;
          color: var(--panel-muted);
        }

        .sidebar__menu-action:hover,
        .sidebar__group-action:hover,
        .sidebar__trigger:hover {
          background: var(--panel-soft);
        }

        .sidebar__rail {
          width: 0.25rem;
          border-radius: 999px;
          background: var(--panel-border);
        }

        .sidebar__inset {
          min-width: 0;
        }

        .sidebar__item-children {
          margin-left: 3rem;
          display: flex;
          flex-direction: column;
          gap: 0.2rem;
        }

        .sidebar__item-children a {
          display: block;
          padding: 0.4rem 0.75rem;
          border-radius: 0.8rem;
        }

        .sidebar__item-children a:hover,
        .sidebar__item-children a[data-active="true"] {
          background: var(--panel-soft);
          color: var(--panel-text);
        }

        .sidebar__footer {
          margin-top: auto;
          padding-top: 1rem;
          border-top: 1px solid var(--panel-border);
        }

        .sidebar__user {
          display: flex;
          align-items: center;
          gap: 0.875rem;
          padding: 0.25rem 0;
        }

        .page {
          padding: 2rem;
        }

        .page__header {
          margin-bottom: 1rem;
        }

        .page__toolbar {
          display: flex;
          align-items: center;
          gap: 0.75rem;
        }

        .page__panel {
          max-width: 56rem;
          padding: 2rem;
          border: 1px solid var(--panel-border);
          border-radius: 1.5rem;
          background: var(--panel-bg);
          box-shadow: var(--shadow);
        }

        .page__pill {
          display: inline-flex;
          padding: 0.35rem 0.7rem;
          border-radius: 999px;
          font-size: 0.8rem;
          font-weight: 700;
          background: var(--content-accent);
          color: var(--panel-accent-text);
        }

        .page__trigger {
          padding: 0.45rem 0.75rem;
          border-radius: 0.75rem;
          background: var(--panel-soft);
        }

        .page__title {
          margin: 0;
          font-size: 2.1rem;
          line-height: 1.15;
        }

        .page__body {
          margin: 1rem 0 0;
          max-width: 42rem;
          color: var(--panel-muted);
          line-height: 1.7;
        }

        @media (max-width: 900px) {
          .app-shell {
            grid-template-columns: 1fr;
          }

          .sidebar {
            border-right: 0;
            border-bottom: 1px solid var(--panel-border);
          }
        }
        """
    )
