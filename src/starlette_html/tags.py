"""HTML tag helper functions for starlette-html."""

from __future__ import annotations

from typing import TYPE_CHECKING

from starlette_html.core import create_element

if TYPE_CHECKING:
    from collections.abc import Callable

    from starlette_html.core import Element


def _tag_factory(tag: str) -> Callable[..., Element]:
    def tag_fn(*children: object, **attrs: object) -> Element:
        return create_element(tag, *children, **attrs)

    tag_fn.__name__ = tag
    tag_fn.__qualname__ = tag
    tag_fn.__doc__ = f"Create a <{tag}> element."
    return tag_fn


a = _tag_factory("a")
article = _tag_factory("article")
aside = _tag_factory("aside")
body = _tag_factory("body")
button = _tag_factory("button")
code = _tag_factory("code")
details = _tag_factory("details")
dialog = _tag_factory("dialog")
div = _tag_factory("div")
em = _tag_factory("em")
footer = _tag_factory("footer")
form = _tag_factory("form")
h1 = _tag_factory("h1")
h2 = _tag_factory("h2")
head = _tag_factory("head")
header = _tag_factory("header")
html = _tag_factory("html")
iframe = _tag_factory("iframe")
img = _tag_factory("img")
input_ = _tag_factory("input")
label = _tag_factory("label")
li = _tag_factory("li")
link = _tag_factory("link")
main = _tag_factory("main")
meta = _tag_factory("meta")
nav = _tag_factory("nav")
p = _tag_factory("p")
path = _tag_factory("path")
script = _tag_factory("script")
section = _tag_factory("section")
small = _tag_factory("small")
span = _tag_factory("span")
strong = _tag_factory("strong")
style = _tag_factory("style")
summary = _tag_factory("summary")
sup = _tag_factory("sup")
svg = _tag_factory("svg")
table = _tag_factory("table")
tbody = _tag_factory("tbody")
td = _tag_factory("td")
textarea = _tag_factory("textarea")
th = _tag_factory("th")
thead = _tag_factory("thead")
time = _tag_factory("time")
title = _tag_factory("title")
tr = _tag_factory("tr")
ul = _tag_factory("ul")
