"""Base layout for the basic example."""

from starlette_html.tags import body, head, html, title


def BaseLayout(
    *children: object,
    page_title: str,
    head_children: tuple[object, ...] = (),
) -> object:
    """Render the shared page shell."""
    return html(
        head(
            title(page_title),
            *head_children,
        ),
        body(*children),
    )
