"""Starlette integration helpers for starlette-html."""

from __future__ import annotations

from typing import TYPE_CHECKING

from starlette.responses import HTMLResponse

if TYPE_CHECKING:
    from starlette.background import BackgroundTask

from starlette_html.core import render, render_document


def html_response(
    node: object,
    *,
    status_code: int = 200,
    headers: dict[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> HTMLResponse:
    """Render a fragment node into a Starlette HTML response."""
    return HTMLResponse(
        render(node),
        status_code=status_code,
        headers=headers,
        media_type=media_type,
        background=background,
    )


def document_response(
    node: object,
    *,
    status_code: int = 200,
    headers: dict[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> HTMLResponse:
    """Render a full document node into a Starlette HTML response."""
    return HTMLResponse(
        render_document(node),
        status_code=status_code,
        headers=headers,
        media_type=media_type,
        background=background,
    )


HTML = html_response
Document = document_response
