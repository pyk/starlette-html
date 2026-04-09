"""Generic UI primitives for the basic example.

Primitives are low-level building blocks: small reusable components that mostly
define structure, styling hooks, and behavior hooks. They accept arbitrary
children and should stay generic enough to be reused across many different app
compositions.

This is different from app components such as `AppSidebar`, which know about
specific application data and product structure like branding, navigation
sections, and signed-in users.
"""

from examples.basic.components.primitives.sidebar import (
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupAction,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarHeader,
    SidebarInset,
    SidebarMenu,
    SidebarMenuAction,
    SidebarMenuBadge,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
    SidebarRail,
    SidebarRoot,
    SidebarStyles,
    SidebarTrigger,
)

__all__ = [
    "Sidebar",
    "SidebarContent",
    "SidebarFooter",
    "SidebarGroup",
    "SidebarGroupAction",
    "SidebarGroupContent",
    "SidebarGroupLabel",
    "SidebarHeader",
    "SidebarInset",
    "SidebarMenu",
    "SidebarMenuAction",
    "SidebarMenuBadge",
    "SidebarMenuButton",
    "SidebarMenuItem",
    "SidebarMenuSub",
    "SidebarMenuSubButton",
    "SidebarMenuSubItem",
    "SidebarRail",
    "SidebarRoot",
    "SidebarStyles",
    "SidebarTrigger",
]
