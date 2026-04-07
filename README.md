# starlette-html

`starlette-html` is a Python-first HTML DSL for
[Starlette](https://starlette.dev/) that helps you build server-rendered UI with
plain Python functions.

It gives you a small, direct way to:

- build HTML in Python
- compose reusable components with normal functions
- pass data as regular function arguments
- render full documents or partial fragments
- return HTML responses directly from routes
- keep escaping safe by default

You might also like my other Starlette packages that I use and maintain:

- [`starlette-hot-reload`](https://github.com/pyk/starlette-hot-reload) - a
  lightweight hot reload utility for Starlette that provides fast in-browser
  reloads for templates and static files.
- [`starlette-tailwindcss`](https://github.com/pyk/starlette-tailwindcss) - a
  lightweight utility for Starlette that builds Tailwind CSS on startup with
  optional watch mode during development.

## Installation

```shell
uv add starlette-html
# or
pip install starlette-html
```

## Example

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette_html import Document, body, h1, head, html, p, title


async def load_user(request):
    return {"name": "Ada", "email": "ada@example.com"}


def HomePage(*, user: dict):
    return html(
        head(title("Home")),
        body(
            h1(f"Hello {user['name']}"),
            p(user["email"]),
        ),
    )


async def homepage(request):
    user = await load_user(request)
    return Document(HomePage(user=user))


app = Starlette(
    routes=[
        Route("/", homepage),
    ]
)
```

## Core idea

The library keeps the model simple.

- HTML tags are Python callables
- components are plain Python functions
- positional arguments become children
- keyword arguments become attributes
- lists and tuples are flattened
- `None` and `False` children are ignored

Example:

```python
from starlette_html import div, h1, p


def UserCard(*, name: str, email: str):
    return div(
        h1(name),
        p(email),
        cls="user-card",
    )
```

## Rendering

Use `render` when you want an HTML fragment.

```python
from starlette_html import li, ul, render


html_fragment = render(
    ul(
        li("One"),
        li("Two"),
    )
)
```

Use `render_document` when you want a full HTML document.

```python
from starlette_html import body, h1, head, html, render_document, title


page = render_document(
    html(
        head(title("Home")),
        body(h1("Hello")),
    )
)
```

## Route helpers

`starlette-html` includes thin response helpers for direct route usage.

```python
from starlette_html import Document, HTML, body, h1, head, html, title


async def homepage(request):
    return Document(
        html(
            head(title("Home")),
            body(h1("Hello")),
        )
    )


async def fragment(request):
    return HTML(h1("Fragment"))
```

## HTMX-friendly attributes

Normal HTML attributes work naturally, including HTMX attributes.

```python
from starlette_html import button


button(
    "Refresh",
    hx_get="/items",
    hx_target="#items",
    hx_swap="outerHTML",
)
```

## Safety

Dynamic text is escaped by default.

If you need to render trusted HTML, wrap it with `Markup`.

```python
from starlette_html import Markup, div


div(Markup("<strong>Hello</strong>"))
```

## License

MIT
