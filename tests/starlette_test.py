"""Starlette integration tests for starlette-html."""

import pytest
from starlette.responses import HTMLResponse

from starlette_html import body, h1, html, p
from starlette_html.starlette import HTML, Document


def home_page(*, user: object) -> object:
    """Build a simple page from a user value."""
    return html(
        body(
            h1(f"Hello {user}"),
            p("Welcome back."),
        )
    )


HomePage = home_page


async def homepage(_request: object) -> HTMLResponse:
    """Return a full document response from a route."""
    user = "Ada"
    return Document(HomePage(user=user))


async def fragment(_request: object) -> HTMLResponse:
    """Return a fragment response from a route."""
    return HTML(h1("Fragment"))


@pytest.mark.asyncio
async def test_document_helper_returns_html_response() -> None:
    """Document should render a full page with a doctype."""
    response = await homepage(object())
    assert isinstance(response, HTMLResponse)
    assert bytes(response.body).decode() == (
        "<!doctype html><html><body><h1>Hello Ada</h1>"
        "<p>Welcome back.</p></body></html>"
    )


@pytest.mark.asyncio
async def test_html_helper_returns_fragment_response() -> None:
    """HTML should render a fragment without a doctype."""
    response = await fragment(object())
    assert isinstance(response, HTMLResponse)
    assert bytes(response.body).decode() == "<h1>Fragment</h1>"
