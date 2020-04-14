# compile.py
#
# Compiles Jingle code to a standalone executable using Clang.  This
# requires the clang compiler to be installed on your machine.  You
# might have to fiddle with some of the path settings and other details
# to make this work.

import subprocess
import sys
import os.path
import tempfile

from .llvmgen import compile_llvm
from .errors import errors_reported

# Name of the runtime library
_rtlib = os.path.join(os.path.dirname(__file__), 'jnruntime.c')

# clang installation
CLANG = 'clang'

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 -m jingle.compile filename\n")
        raise SystemExit(1)

    source = open(sys.argv[1]).read()
    llvm_code = compile_llvm(source)
    if not errors_reported():
        with tempfile.NamedTemporaryFile(suffix='.ll') as f:
            f.write(llvm_code.encode('utf-8'))
            f.flush()
            # subprocess.check_output([CLANG,  f.name, _rtlib])
            head, tail = os.path.split(sys.argv[1])
            if len(head) < 1:
                head = "local folder"
            output_name = os.path.splitext(sys.argv[1])[0]+".exe"

            subprocess.check_output([CLANG, '-o', output_name, '-DNEED_MAIN', f.name, _rtlib])
            print("Wrote "+output_name+" to "+head)

if __name__ == '__main__':
    main()
