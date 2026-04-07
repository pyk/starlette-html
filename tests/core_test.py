"""Core rendering tests for starlette-html."""

from starlette_html import (
    Fragment,
    Markup,
    article,
    aside,
    body,
    button,
    code,
    div,
    h1,
    header,
    iframe,
    input_,
    label,
    link,
    main,
    nav,
    render,
    render_document,
    section,
    style,
    textarea,
)


def test_render_escapes_text_and_renders_document() -> None:
    """Text should be escaped and documents should include a doctype."""
    assert render(div("<script>alert(1)</script>")) == (
        "<div>&lt;script&gt;alert(1)&lt;/script&gt;</div>"
    )
    assert render_document(body(h1("Hello"))) == (
        "<!doctype html><body><h1>Hello</h1></body>"
    )


def test_render_handles_attributes_and_fragments() -> None:
    """Attributes and fragments should render with HTMX-friendly names."""
    node = Fragment(
        div("A", cls="card", data_theme="dark"),
        input_(type="checkbox", checked=True),
        button("Refresh", hx_get="/items", hx_target="#items"),
    )

    assert render(node) == (
        '<div class="card" data-theme="dark">A</div>'
        '<input type="checkbox" checked />'
        '<button hx-get="/items" hx-target="#items">Refresh</button>'
    )


def test_markup_is_rendered_verbatim() -> None:
    """Markup should render without escaping."""
    assert render(Markup("<strong>Hello</strong>")) == "<strong>Hello</strong>"


def test_render_supports_additional_html_elements() -> None:
    """New element helpers should render their corresponding HTML tags."""
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
        "<style>body { color: red; }</style>"
        '<link rel="stylesheet" href="/app.css" />'
        "</main>"
    )
