"""Base layout for the basic example."""

from starlette_html import body, head, html, title


def BaseLayout(*children: object, page_title: str) -> object:
    """Render the shared page shell."""
    return html(
        head(title(page_title)),
        body(*children),
    )
