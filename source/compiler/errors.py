# errors.py

import sys
from colorama import init, Fore, Back, Style
init()

_num_errors = 0

def error(lineno, message, filename=None):
    '''
    Report a compiler error to all subscribers
    '''
    global _num_errors
    if not filename:
        errmsg = f"{Fore.RED}Error:{Style.RESET_ALL} {message}, line {lineno}"
    else:
        errmsg = f"{Fore.RED}Error:{Style.RESET_ALL} {message}, line {lineno}, file {filename}"

    print(errmsg, file=sys.stderr)
    _num_errors += 1

def errors_reported():
    '''
    Return number of errors reported
    '''
    return _num_errors

def clear_errors():
    '''
    Clear the total number of errors reported.
    '''
    global _num_errors
    _num_errors = 0
