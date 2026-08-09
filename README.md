# cli-fw

A compact dataclass-driven command-line framework extracted from the Pacman and
RAG projects.

```bash
uv add cli-fw
```

## Example

```python
from dataclasses import dataclass
from cli_fw import Command, arg


@dataclass
class Serve:
    port: int = arg(help="Port to listen on", default=8000)


command = Command("serve", schema=Serve)
parsed = command.execute(["--port", "8080"])
```

It supports positional and optional arguments, choices, booleans, lists,
nested commands, generated help, and typed parse errors.

## Dependencies

- Python 3.10+
- `typed-errs` for `Result`, `Err`, and diagnostics

## Development and release

Run `mise run check`. Every push to `master` publishes a unique `0.0.<CI run>` ZeroVer
version through PyPI Trusted Publishing. `mise run publish` remains available.
