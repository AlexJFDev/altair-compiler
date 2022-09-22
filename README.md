#### This program assembles binary files for the Altair 8800.
##### VERSION 1.1.3

### How to use

Run the file main.py with (probably) any version of Python3 like this:
> python3 main.py {program.file} {output.location}(optional)

### Writing programs

Bytes are written in the same order as on the file. Some instructions will take up multiple bytes with arguments so keep that in mind.

Comments can be made with #

To write instructions use the Mnemonic found in the manual followed by any arguments that an instruction takes. Arguments are separated from the instruction, and each other, by commas.
* Instructions that have arguments "in byte" take arguments in binary form.
* Instructions that have arguments in the next one or two bytes take arguments in hex form.
* The MOV instruction takes arguments in the form of B, C, D, E, H, L, M, and A. A references the accumulator and M references a byte in memory at the location H&L point to.

dat (data) is a special instruction. It is not a real Altair 8800 instruction instead it is used to write bytes of data for your program.

### Technical

Info about how the assembler works is available on [my website](https://alexjf.dev/blog/csc205/altair_compiler/index.html).

Adding {print-debugs} to the end of the command when running will print debug info.
