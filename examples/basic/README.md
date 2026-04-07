# Basic Example

This example shows the smallest Starlette app setup for `starlette-html`.

## Run

```shell
uv run uvicorn examples.basic:app --reload
```

The app uses Uvicorn reload mode, so changes to the example files are picked up
automatically during development.

## What it demonstrates

- a Starlette route returning `Document(...)`
- a reusable Python component in `examples/basic/pages`
- a shared layout component in `examples/basic/layouts`
- plain Python data passed into the component as function arguments
