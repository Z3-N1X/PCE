"""
The Core class handles argument parsing using the argparse library.
"""
import os
import keyboard

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
            self.current_pos = 0

            self.render_dir_childs()

            keyboard.add_hotkey("up", self._up_key_pressed)
            keyboard.add_hotkey("down", self._down_key_pressed)

        keyboard.wait("esc")

    def render_dir_childs(self):
        os.system("cls" if os.name == "nt" else "clear")

        dirs_in_current_dir: list[list] = [ [x,"dir"] for x in next(os.walk('.'))[1]]
        file_names: list[list] = [ [x,"file"] for x in next(os.walk("."), (None, None, []))[2]]  # [] if no file

        all_childs = dirs_in_current_dir + file_names

        self.all_childs_len = len(all_childs)

        child_num = 0
        for child in all_childs:
            if child[1] == "file":
                self.log.file(child[0], self.current_pos == child_num)
            if child[1] == "dir":
                self.log.folder(child[0], self.current_pos == child_num)
            
            child_num += 1

    def _up_key_pressed(self):
        if self.current_pos == 0:
            return
        self.current_pos -= 1    
        self.render_dir_childs()  

    def _down_key_pressed(self):
        if self.current_pos == self.all_childs_len - 1:
            return
        self.current_pos += 1    
        self.render_dir_childs()  

    def add_args(self):
        """
        Adds arguemnets to parser.
        """
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
