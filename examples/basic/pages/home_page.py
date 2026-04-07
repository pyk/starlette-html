"""Page components for the basic example."""

from examples.basic.layouts import BaseLayout
from starlette_html import h1, p


def HomePage(*, user: dict[str, str]) -> object:
    """Render the homepage."""
    return BaseLayout(
        h1(f"Hello {user['name']}"),
        p(user["email"]),
        page_title="Home",
    )
