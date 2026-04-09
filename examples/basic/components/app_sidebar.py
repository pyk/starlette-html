"""App-specific sidebar composition for the basic example.

This module sits above the sidebar primitives layer.

Where the primitives define generic building blocks such as `Sidebar`,
`SidebarHeader`, and `SidebarMenu`, this module composes those pieces into a
concrete application sidebar with opinions about branding, navigation sections,
badges, and the signed-in user.

Use this layer when you want to turn application data into a ready-to-render
sidebar. Use the primitives layer when you want generic, reusable building
blocks that can be rearranged and customized for many different applications.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from examples.basic.components.primitives import (
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuAction,
    SidebarMenuBadge,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
)
from starlette_html.tags import a, div, p, span


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


def AppSidebar(
    *,
    brand_name: str,
    brand_plan: str,
    sections: tuple[SidebarSection, ...],
    user: SidebarUser,
) -> object:
    """Render the app-specific composed sidebar."""
    return Sidebar(
        SidebarHeader(
            div(
                span(brand_name[:2].upper(), cls="sidebar__brand-mark"),
                div(
                    p(brand_name, cls="sidebar__title"),
                    p(brand_plan, cls="sidebar__eyebrow"),
                ),
                cls="sidebar__brand",
            ),
        ),
        SidebarContent(
            [_AppSidebarSection(section_data=section) for section in sections],
        ),
        SidebarFooter(
            div(
                span(user.initials, cls="sidebar__user-avatar"),
                div(
                    p(user.name, cls="sidebar__user-name"),
                    p(user.email, cls="sidebar__user-email"),
                ),
                cls="sidebar__user",
            ),
        ),
    )


def _AppSidebarSection(*, section_data: SidebarSection) -> object:
    return SidebarGroup(
        SidebarGroupLabel(section_data.title),
        SidebarGroupContent(
            SidebarMenu(
                [_AppSidebarItem(item=item) for item in section_data.items],
            ),
        ),
    )


def _AppSidebarItem(*, item: SidebarItem) -> object:
    return SidebarMenuItem(
        SidebarMenuButton(
            span(item.icon or item.label[:1].upper(), cls="sidebar__item-icon"),
            span(item.label, cls="sidebar__item-label"),
            item.badge and SidebarMenuBadge(item.badge),
            active=item.active,
            render_as=a(href=item.href),
        ),
        SidebarMenuAction(
            "Open",
            aria_label=f"Open actions for {item.label}",
        ),
        item.children
        and SidebarMenuSub(
            [
                SidebarMenuSubItem(
                    SidebarMenuSubButton(
                        child.label,
                        active=child.active,
                        render_as=a(href=child.href),
                    )
                )
                for child in item.children
            ],
        ),
    )
