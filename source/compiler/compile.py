# compile.py

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
        sys.stderr.write("Usage: python3 -m gone.compile filename\n")
        raise SystemExit(1)

    source = open(sys.argv[1]).read()
    llvm_code = compile_llvm(source)
    if not errors_reported():
        with tempfile.NamedTemporaryFile(suffix='.ll') as f:
            f.write(llvm_code.encode('utf-8'))
            f.flush()
            # subprocess.check_output([CLANG,  f.name, _rtlib])

            subprocess.check_output([CLANG, '-DNEED_MAIN', f.name, _rtlib])

if __name__ == '__main__':
    main()
