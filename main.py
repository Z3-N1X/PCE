from sys import argv
import os



file_name = argv[1] if len(argv) > 1 else None
file_text = open(f"{os.getcwd()}/{file_name}", "r").read()

os.system("cls")
print(file_text, end="\r")
