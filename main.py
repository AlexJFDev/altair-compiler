"""
Main module for the Altair 8800 compiler
This script compiles binary files for the Altair 8800. See the README for details
"""

import sys
from compiler import Compiler

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) == 0:
        print("an input file location was not passed as an argument")
        print("STOPPING COMPILER")
        sys.exit()
    elif len(sys.argv) == 2:
        compiler = Compiler(sys.argv[1][0:sys.argv[1].rfind(".")])
        compiler.compile()
        compiler.write()
    elif len(sys.argv) == 3:
        compiler = Compiler(sys.argv[1], _output_file_location = sys.argv[2])
        compiler.compile()
        compiler.write()
    else:
        print("too many arguments were provided\nplease try again with up to two arguments")
        print("STOPPING COMPILER")
        sys.exit()
