import argparse

welcomeMessage = "Jingle 2019 v0.01-rc1 - (c) Millo Evers"
parser = argparse.ArgumentParser(description=welcomeMessage)
subparsers = parser.add_subparsers(help='sub commands')

parser.add_argument('-version', required=False, help='view version number of your Jingle installation and view info on updating')
parser.add_argument('-compile', required=False, help='compile Jingle code to a variety of different targets to be executed later')
parser.add_argument('-run', required=False, help='JIT-compile Jingle code and run instantly, without creating an executable')

parser.parse_args()
