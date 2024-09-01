"""
The Core class handles argument parsing using the argparse library.
"""
import os

from .loging.log import Log
from .argparser import ArgParser

class Core:
    """
    The Core class handles argument parsing using the argparse library.
    """

    def __init__(self):
        self.parser = ArgParser()
        self.add_args()
        self.log= Log()

    def start(self):
        """
        Starts the Core class by creating the argument parser 
        and parsing the command-line arguments.
        """

        file_name = self.parser.filename
        if file_name:
            self._print_file_content(file_name)
        else: 
            print(next(os.walk('.'))[1])

    def add_args(self):
        self.parser.add_argument("filename", nargs="?")

    def _print_file_content(self, file_name: str):
        """prints file content

        Args:
            file_name (str): _description_
        """
        try:
            with open(os.path.join(os.getcwd(), file_name), 'r', encoding='utf-8') as file:
                file_text = file.read()
                os.system("cls" if os.name == "nt" else "clear")
                print(file_text, end="\r")
        except FileNotFoundError:
            self.log.error(f"Error: File '{file_name}' not found.")
            return
        except Exception as e:
            self.log.error(f"Error: {e}")
            return
