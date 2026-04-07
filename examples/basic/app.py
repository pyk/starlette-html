"""Basic Starlette app example for starlette-html."""

from __future__ import annotations

import logging
import sys
from typing import TYPE_CHECKING

import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route

from examples.basic.pages import HomePage
from starlette_html import Document

# Enable debug logging to stderr
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stderr,
)

if TYPE_CHECKING:
    from starlette.requests import Request
    from starlette.responses import HTMLResponse


async def homepage(_request: Request) -> HTMLResponse:
    """Homepage handler."""
    user = {"name": "Ada", "email": "ada@example.com"}
    return Document(HomePage(user=user))


routes = [
    Route("/", homepage),
]


app = Starlette(
    debug=True,
    routes=routes,
)

if __name__ == "__main__":
    uvicorn.run(
        "examples.basic:app",
        host="127.0.0.1",
        port=3000,
        reload=True,
        log_config=None,
    )
