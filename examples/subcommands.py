"""A complete CLI with typed schemas, subcommands, and callbacks."""

from dataclasses import dataclass
from pathlib import Path

from typed_errs import Err

from cli_fw import Command, arg


@dataclass
class Index:
    """Arguments accepted by the index subcommand."""

    source: Path = arg(positional=True, help="Directory to index")
    workers: int = arg(default=4, help="Number of indexing workers")
    verbose: bool = arg(default=False, help="Print every indexed path")


def run_index(options: Index) -> int:
    """Execute the index command after parsing succeeds."""
    print(f"indexing {options.source} with {options.workers} workers")
    return 0


@dataclass
class Search:
    """Arguments accepted by the search subcommand."""

    query: str = arg(positional=True, help="Text to search for")
    limit: int = arg(default=10, help="Maximum number of matches")


root = Command("project", short="Index and search a project")
root.add_command(Command("index", schema=Index, run=run_index))
root.add_command(Command("search", schema=Search, run=lambda options: print(options)))

result = root.execute()
if isinstance(result, Err):
    result.print_diagnostic()
    raise SystemExit(2)
