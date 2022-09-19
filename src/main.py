"""
Main module for the Altair 8800 assembler
This script assembles binary files for the Altair 8800. See the README for details
"""

import sys
from altair_assembler import Assembler

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("an input file location was not passed as an argument")
        print("STOPPING ASSEMBLER")
        sys.exit()
    elif len(sys.argv) == 2:
        assembler = Assembler(sys.argv[1], False)
    elif len(sys.argv) == 3:
        if sys.argv[2] == "-print-debugs":
            assembler = Assembler(sys.argv[1], True)
        else:
            assembler = Assembler(sys.argv[1], False, _output_file_location = sys.argv[2])
    elif len(sys.argv) >= 4:
        if sys.argv[3] == "-print-debugs":
            assembler = Assembler(sys.argv[1], True, _output_file_location = sys.argv[2])
        else:
            assembler = Assembler(sys.argv[1], False, _output_file_location = sys.argv[2])
    assembler.assemble()
    assembler.write()
    if len(sys.argv) >4:
        print("extra arguments were provided and ignored")
