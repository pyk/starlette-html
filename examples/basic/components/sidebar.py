"""Composable sidebar components for the basic example app."""

from __future__ import annotations

from dataclasses import dataclass, field

from starlette_html.tags import (
    a,
    aside,
    div,
    header,
    li,
    nav,
    p,
    section,
    span,
    style,
    ul,
)


@dataclass(frozen=True, slots=True)
class SidebarItem:
    """A navigation item that can render links and nested links."""

    label: str
    href: str = "#"
    icon: str | None = None
    active: bool = False
    badge: str | None = None
    children: tuple[SidebarItem, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class SidebarSection:
    """A titled group of sidebar navigation items."""

    title: str
    items: tuple[SidebarItem, ...]


@dataclass(frozen=True, slots=True)
class SidebarUser:
    """Profile information displayed in the sidebar footer."""

    name: str
    email: str
    initials: str


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

        .sidebar__item-link {
          display: flex;
          align-items: center;
          gap: 0.75rem;
          min-height: 3rem;
          padding: 0.65rem 0.75rem;
          border-radius: 1rem;
          color: var(--panel-text);
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
          margin-bottom: 1rem;
          padding: 0.35rem 0.7rem;
          border-radius: 999px;
          font-size: 0.8rem;
          font-weight: 700;
          background: var(--content-accent);
          color: var(--panel-accent-text);
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


def Sidebar(
    *,
    brand_name: str,
    brand_plan: str,
    sections: tuple[SidebarSection, ...],
    user: SidebarUser,
) -> object:
    """Render a customizable application sidebar."""
    return aside(
        header(
            div(
                span(brand_name[:2].upper(), cls="sidebar__brand-mark"),
                div(
                    p(brand_name, cls="sidebar__title"),
                    p(brand_plan, cls="sidebar__eyebrow"),
                ),
                cls="sidebar__brand",
            ),
            cls="sidebar__header",
        ),
        nav(
            [_SidebarSection(section_data=section) for section in sections],
            cls="sidebar__nav",
        ),
        div(
            div(
                span(user.initials, cls="sidebar__user-avatar"),
                div(
                    p(user.name, cls="sidebar__user-name"),
                    p(user.email, cls="sidebar__user-email"),
                ),
                cls="sidebar__user",
            ),
            cls="sidebar__footer",
        ),
        cls="sidebar",
    )


def _SidebarSection(*, section_data: SidebarSection) -> object:
    return section(
        p(section_data.title, cls="sidebar__section-title"),
        ul(
            [_SidebarItem(item=item) for item in section_data.items],
            cls="sidebar__items",
        ),
        cls="sidebar__section",
    )


def _SidebarItem(*, item: SidebarItem) -> object:
    return li(
        a(
            span(item.icon or item.label[:1].upper(), cls="sidebar__item-icon"),
            span(item.label, cls="sidebar__item-label"),
            item.badge and span(item.badge, cls="sidebar__item-badge"),
            href=item.href,
            cls="sidebar__item-link",
            data_active=str(item.active).lower(),
            aria_current="page" if item.active else None,
        ),
        item.children
        and ul(
            [
                li(
                    a(
                        child.label,
                        href=child.href,
                        data_active=str(child.active).lower(),
                        aria_current="page" if child.active else None,
                    )
                )
                for child in item.children
            ],
            cls="sidebar__item-children",
        ),
        cls="sidebar__item",
    )
