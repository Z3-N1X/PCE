"""
The Core class handles argument parsing using the argparse library.
"""
import argparse
import os

from .loging.log import Log

class Core:
    """
    The Core class handles argument parsing using the argparse library.
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='PCE',
            description='Python CLI Editor',
            epilog='Use vozicode -help'
        )
        self.log= Log()

    def _create_arg_parser(self):
        """
        Creates an argument parser and adds the filename argument.
        """
        self.parser.add_argument('filename')

    def parse_args(self):
        """
        Parses the command-line arguments using the argument parser.
        """
        try:
            args = self.parser.parse_args()
            return args
        except SystemExit:
            return None
        except Exception as e:
            self.log.error(f"Error: {e}")
            return None

    def start(self):
        """
        Starts the Core class by creating the argument parser 
        and parsing the command-line arguments.
        """
        self._create_arg_parser()
        args = self.parse_args()
        if args:
            file_name = args.filename

            try:
                with open(os.path.join(os.getcwd(), file_name), 'r', encoding='utf-8') as file:
                    file_text = file.read()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(file_text, end="\r")
            except FileNotFoundError:
                self.log.error(f"Error: File '{file_name}' not found.")
                return
            except Exception as e:
                self.log.error(f"Error: {e}")
                return
