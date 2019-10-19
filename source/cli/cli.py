import argparse

parser = argparse.ArgumentParser(description='Access the Jingle programming language.')
parser.add_argument('compile', metavar='bc',
                    help='Compile Jingle code.')
parser.add_argument('--llvm',
                    help='Compile Jingle code to LLVM IR')

args = parser.parse_args
print(args)
