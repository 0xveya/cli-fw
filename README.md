# cli-fw

[![PyPI](https://img.shields.io/pypi/v/cli-fw)](https://pypi.org/project/cli-fw/)
[![CI](https://github.com/0xveya/cli-fw/actions/workflows/ci.yml/badge.svg)](https://github.com/0xveya/cli-fw/actions/workflows/ci.yml)

**[View cli-fw on PyPI](https://pypi.org/project/cli-fw/)**

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

Parse failures return `Err[CliError]`. Their source diagnostic is stored as
`Option[Diagnostic]`, and a diagnostic help message is `Option[str]`; use
`isinstance(value, Some)` when inspecting either field directly, or call
`Err.print_diagnostic()` to render it.

## Commands and subcommands

Define arguments in dataclasses, attach each schema to a `Command`, then call
`execute()`. A command callback receives the validated dataclass instance. A
root command can contain any number of subcommands:

```python
root = Command("project", short="Index and search a project")
root.add_command(Command("index", schema=Index, run=run_index))
root.add_command(Command("search", schema=Search, run=run_search))
result = root.execute()
```

Run it like `python app.py index ./src --workers 8`, or add `--help` at any
command level. See the complete runnable
[subcommand example](examples/subcommands.py), including positional values,
defaults, boolean flags, callbacks, and diagnostic handling.

## Where I use it

This is my internal CLI framework for 42 projects. The latest implementation
was extracted from
[Pacman](https://github.com/Valentins-and-Veyas-42-group-projects/pac-man), a
work-in-progress group project in the 42 organization,
with behavior checked against
[RAG Against the Machine](https://github.com/0xveya/42-rag-against-the-machine).
Pacman uses it for the game command and RAG uses it to validate command syntax
and produce diagnostics before command execution.

## Dependencies

- Python 3.10+
- `typed-errs` for `Result`, `Err`, and diagnostics

## Use and contributions

This is a personal library, but it is not private or locked to my projects.
You may use it in general Python work and in 42 projects under the MIT license;
just follow the rules that apply to your campus and assignment.

Contributions are welcome: open an issue or send a pull request. I do not care
whether a contribution is written by hand, AI-assisted, or generated another
way; I care about whether it is correct, tested, understandable, and a good fit.
Because this is opinionated personal infrastructure, pull requests are reviewed
selectively and are likely to be rejected unless they clearly improve the
library without making it harder to maintain.

## Development and release

Run `mise run check`. Every push to `master` publishes a unique `0.0.<CI run>` ZeroVer
version through PyPI Trusted Publishing. `mise run publish` remains available.
