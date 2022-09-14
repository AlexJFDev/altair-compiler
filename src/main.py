"""
Main module for the Altair 8800 compiler
This script compiles binary files for the Altair 8800. See the README for details
"""

import sys
from altairCompiler import Compiler

if __name__ == "__main__":
    if len(sys.argv) == 0:
        print("an input file location was not passed as an argument")
        print("STOPPING COMPILER")
        sys.exit()
    elif len(sys.argv) == 2:
        compiler = Compiler(sys.argv[1], False)
        compiler.compile()
        compiler.write()
    elif len(sys.argv) == 3:
        compiler = Compiler(sys.argv[1], False, _output_file_location = sys.argv[2])
        compiler.compile()
        compiler.write()
    elif len(sys.argv) >= 4:
        if sys.argv[3] == "print-debugs":
            compiler = Compiler(sys.argv[1], True, _output_file_location = sys.argv[2])
        else:
            compiler = Compiler(sys.argv[1], True, _output_file_location = sys.argv[2])
        compiler.compile()
        compiler.write()
    if len(sys.argv) >4:
        print("extra arguments were provided and ignored")
