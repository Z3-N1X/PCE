try:
    from sys import argv
    import os
    import argparse
except:
    raise ImportError


parser = argparse.ArgumentParser(
                    prog='PCE',
                    description='Python CLI Editor',
                    epilog='Use vozicode -help'
)

parser.add_argument('filename')

args = parser.parse_args()
file_name = args.filename

file_text = open(f"{os.getcwd()}/{file_name}", "r").read()

os.system("cls")
print(file_text, end="\r")
