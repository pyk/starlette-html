# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-04-07

### Added

- Support additional HTML tag helpers: `main`, `section`, `style`, `nav`,
  `aside`, `header`, `article`, `code`, `label`, `textarea`, `iframe`, and
  `link`.

## [0.1.0] - 2026-04-07

### Added

- Initial release of `starlette-html`.
- Python-first HTML DSL with function-based components.
- Core HTML tag helpers including `div`, `span`, `h1`, `p`, `ul`, `li`, `a`,
  `button`, `input_`, `html`, `head`, `body`, `title`, `meta`, and `script`.
- Safe-by-default rendering with HTML escaping and explicit `Markup` support for
  trusted HTML.
- Fragment rendering with `Fragment`, `render`, and `render_document`.
- Attribute normalization for Python-friendly names such as `cls`, `for_`, and
  `data_theme`.
- Boolean attribute rendering and omission of `None` and `False` values.
- Starlette response helpers via `HTML` and `Document`.
- HTMX-friendly attribute rendering through normal HTML attributes.

[Unreleased]: https://github.com/pyk/starlette-html/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/pyk/starlette-html/releases/tag/v0.2.0
[0.1.0]: https://github.com/pyk/starlette-html/releases/tag/v0.1.0
