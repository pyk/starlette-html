"""Tag helper tests for starlette-html."""

from starlette_html import render
from starlette_html.tags import (
    article,
    aside,
    code,
    details,
    dialog,
    em,
    footer,
    form,
    header,
    iframe,
    img,
    label,
    link,
    main,
    nav,
    path,
    section,
    small,
    strong,
    style,
    summary,
    sup,
    svg,
    table,
    tbody,
    td,
    textarea,
    th,
    thead,
    time,
    tr,
)


def test_tag_helpers_render_existing_semantic_elements() -> None:
    """Existing tag helpers should render their corresponding HTML tags."""
    node = main(
        header("Header"),
        nav("Nav"),
        article(
            section(
                aside("Aside"),
                code("print('hello')"),
                label("Message", for_="message"),
                textarea("Hello", id="message"),
                iframe(src="/frame"),
            )
        ),
        footer("Footer"),
        style("body { color: red; }"),
        link(rel="stylesheet", href="/app.css"),
    )

    assert render(node) == (
        "<main>"
        "<header>Header</header>"
        "<nav>Nav</nav>"
        "<article>"
        "<section>"
        "<aside>Aside</aside>"
        "<code>print(&#x27;hello&#x27;)</code>"
        '<label for="message">Message</label>'
        '<textarea id="message">Hello</textarea>'
        '<iframe src="/frame"></iframe>'
        "</section>"
        "</article>"
        "<footer>Footer</footer>"
        "<style>body { color: red; }</style>"
        '<link rel="stylesheet" href="/app.css" />'
        "</main>"
    )


def test_tag_helpers_render_phase_one_tags() -> None:
    """Phase 1 tag helpers should cover richer UI markup."""
    node = form(
        details(
            summary("Shipping details"),
            small("Updated "),
            time("today", datetime="2026-04-08"),
        ),
        table(
            thead(
                tr(
                    th("Plan"),
                    th("Seats"),
                )
            ),
            tbody(
                tr(
                    td(strong("Enterprise")),
                    td(sup("*"), "24"),
                )
            ),
        ),
        dialog(
            em("Confirm upgrade"),
            open=True,
        ),
        svg(
            path(d="M0 0 L10 10", stroke="currentColor"),
            viewBox="0 0 10 10",
            fill="none",
        ),
        img(src="/logo.png", alt="Logo"),
        action="/upgrade",
        method="post",
    )

    assert render(node) == (
        '<form action="/upgrade" method="post">'
        "<details>"
        "<summary>Shipping details</summary>"
        "<small>Updated </small>"
        '<time datetime="2026-04-08">today</time>'
        "</details>"
        "<table>"
        "<thead><tr><th>Plan</th><th>Seats</th></tr></thead>"
        "<tbody><tr><td><strong>Enterprise</strong></td><td><sup>*</sup>24</td></tr></tbody>"
        "</table>"
        "<dialog open><em>Confirm upgrade</em></dialog>"
        '<svg viewBox="0 0 10 10" fill="none">'
        '<path d="M0 0 L10 10" stroke="currentColor"></path>'
        "</svg>"
        '<img src="/logo.png" alt="Logo" />'
        "</form>"
    )
