"""
The main file starts the Core class and parses the command-line arguments.

This module is the entry point of the program, 
and it is responsible for initializing and starting the Core object.

It imports the necessary modules, 
defines the main function, 
and checks if the script is being run directly or being imported.
"""
from core import Core

def main():
    """
    Executes the main function of the program.

    This function initializes and starts the Core object, 
    which is responsible for running the main logic of the program.

    """
    Core().start()


if __name__ == "__main__":
    main()
