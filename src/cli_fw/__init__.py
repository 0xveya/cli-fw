"""Dataclass-driven command-line parsing."""

from .parser import (
    Action,
    Arg,
    CliError,
    Command,
    HelpMenuStyle,
    Parser,
    arg,
)

__all__ = [
    "Action",
    "Arg",
    "CliError",
    "Command",
    "HelpMenuStyle",
    "Parser",
    "arg",
]
