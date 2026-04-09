"""Page components for the basic example."""

from examples.basic.components import (
    AppSidebar,
    SidebarInset,
    SidebarItem,
    SidebarSection,
    SidebarStyles,
    SidebarTrigger,
    SidebarUser,
)
from examples.basic.layouts import BaseLayout
from starlette_html.tags import div, h1, header, p, span


def HomePage(*, user: dict[str, str]) -> object:
    """Render the homepage."""
    sidebar = AppSidebar(
        brand_name="Acme Inc",
        brand_plan="Enterprise",
        sections=(
            SidebarSection(
                title="Platform",
                items=(
                    SidebarItem(
                        label="Playground",
                        href="#playground",
                        icon="PL",
                        active=True,
                        children=(
                            SidebarItem(label="History", href="#history"),
                            SidebarItem(label="Starred", href="#starred"),
                            SidebarItem(
                                label="Settings",
                                href="#settings",
                                active=True,
                            ),
                        ),
                    ),
                    SidebarItem(label="Models", href="#models", icon="AI"),
                    SidebarItem(label="Documentation", href="#docs", icon="BK"),
                    SidebarItem(label="Settings", href="#app-settings", icon="ST"),
                ),
            ),
            SidebarSection(
                title="Projects",
                items=(
                    SidebarItem(
                        label="Design Engineering",
                        href="#design-engineering",
                        icon="DE",
                    ),
                    SidebarItem(
                        label="Sales & Marketing",
                        href="#sales-marketing",
                        icon="SM",
                        badge="12",
                    ),
                    SidebarItem(label="Travel", href="#travel", icon="TV"),
                ),
            ),
        ),
        user=SidebarUser(
            name=user["name"],
            email=user["email"],
            initials="AD",
        ),
    )

    return BaseLayout(
        div(
            sidebar,
            SidebarInset(
                header(
                    div(
                        SidebarTrigger("Toggle", cls="page__trigger"),
                        span("Sidebar primitives demo", cls="page__pill"),
                        cls="page__toolbar",
                    ),
                    cls="page__header",
                ),
                div(
                    h1("A first pass at a composable sidebar", cls="page__title"),
                    p(
                        "This example pushes starlette-html beyond simple pages into "
                        "reusable application shell components. The sidebar itself is "
                        "assembled from plain Python functions and small data objects, "
                        "which makes the friction points in the DSL much easier "
                        "to see.",
                        cls="page__body",
                    ),
                    p(
                        f"Signed in as {user['name']} ({user['email']}). "
                        "The active navigation state, nested items, badges, and footer "
                        "profile are all driven by regular Python data.",
                        cls="page__body",
                    ),
                    cls="page__panel",
                ),
                cls="page",
            ),
            cls="app-shell",
        ),
        page_title="Home",
        head_children=(SidebarStyles(),),
    )
