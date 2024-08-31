"""
argparser.py

Module for parsing command-line arguments.

Classes:
    ArgParser: A class for parsing command-line arguments.

Functions:
    parse_args: Parse command-line arguments and return a namespace object.
"""
import argparse
from argparse import _FormatterClass, ArgumentParser
from collections.abc import Sequence
from typing import Any

class ArgParser(argparse.ArgumentParser):
    """
    A subclass that provides methods for parsing command-line arguments.

    Attributes:
        None

    Methods:
        _add_args: Adds arguments to the parser.
    """
    def __init__(self,
                 prog: str | None = None,
                 usage: str | None = None,
                 description: str | None = None,
                 epilog: str | None = None,
                 parents: Sequence[ArgumentParser] = ...,
                 formatter_class: _FormatterClass = ...,
                 prefix_chars: str = "-",
                 fromfile_prefix_chars: str | None = None,
                 argument_default: Any = None,
                 conflict_handler: str = "error",
                 add_help: bool = True,
                 allow_abbrev: bool = True,
                 exit_on_error: bool = True
                ) -> None:

        prog = "PCI"
        description = "Python CLI Editor"
        epilog = f"Use {prog.lower()} -help"

        super().__init__(prog,
                         usage,
                         description,
                         epilog,
                         parents,
                         formatter_class,
                         prefix_chars,
                         fromfile_prefix_chars,
                         argument_default,
                         conflict_handler,
                         add_help,
                         allow_abbrev,
                         exit_on_error
                        )

    def _add_args(self):
        self.add_argument("filename")
