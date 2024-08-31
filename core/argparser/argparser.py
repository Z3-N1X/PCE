"""
argparser.py

Module for parsing command-line arguments.

Classes:
    ArgParser: A class for parsing command-line arguments.

Functions:
    parse_args: Parse command-line arguments and return a namespace object.
"""
import argparse

class ArgParser(argparse.ArgumentParser):
    """
    A subclass that provides methods for parsing command-line arguments.

    Attributes:
        None

    Methods:
        _add_args: Adds arguments to the parser.
    """
    def __init__(self) -> None:

        prog = "PCI"
        description = "Python CLI Editor"
        epilog = f"Use {prog.lower()} -help"

        self._add_args()

        super().__init__(prog=prog,
                         description=description,
                         epilog=epilog,
                        )

    def _add_args(self):
        self.add_argument("filename")

    @property
    def filename(self):
        """filename property.

        Returns:
            _type_: _description_
        """
        return self.parse_args().filename
