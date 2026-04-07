"""Page components for the basic example."""

from starlette_html import body, h1, head, html, p, title


def HomePage(*, user: dict[str, str]) -> object:
    """Render the homepage."""
    return html(
        head(title("Home")),
        body(
            h1(f"Hello {user['name']}"),
            p(user["email"]),
        ),
    )
