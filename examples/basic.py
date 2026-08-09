from dataclasses import dataclass

from cli_fw import Command, arg


@dataclass
class Greet:
    name: str = arg(positional=True, help="Person to greet")
    loud: bool = arg(default=False, help="Use uppercase output")


print(Command("greet", schema=Greet).execute())
