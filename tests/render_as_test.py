"""Render target composition tests for starlette-html."""

import pytest

from starlette_html import render, render_as
from starlette_html.tags import a, h1


def test_render_as_merges_classes_and_children() -> None:
    """Render targets should keep their tag and merge attrs predictably."""
    node = render_as(
        a(href="/settings", cls="link-base"),
        default_tag="button",
        children=(h1("Settings"),),
        attrs={
            "cls": ["sidebar__item-link", "active"],
            "data_active": "true",
        },
    )

    assert render(node) == (
        '<a href="/settings" class="link-base sidebar__item-link active" '
        'data-active="true"><h1>Settings</h1></a>'
    )


def test_render_as_rejects_non_element_targets() -> None:
    """Render targets should be real elements."""
    with pytest.raises(TypeError):
        render_as(
            "/settings",
            default_tag="button",
            children=("Settings",),
        )
