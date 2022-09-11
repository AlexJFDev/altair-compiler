####This program compiles binary files for the altair 8800.

### How to use

Run the file main.py with (probably) any version of Python3 like this:
> python3 main.py {program.file} {output.location}(optional)

### Writing programs

Bytes are written in the same order as on the file. Some instructions will take up multiple bytes with arguments so keep that in mind.

Comments can be made with #

To write code use the Mnemonic found in the manual followed by any arguments that an instruction takes. Arguments are separated from the instruction, and each other, by commas.
* Instructions that have arguments "in byte" take arguments in binary form.
* Instructions that have arguments in the next one or two bytes take arguments in hex form.
* The MOV instruction takes arguments in the form of B, C, D, E, H, L, M, and A. A references the accumulator and M references a byte in memory at the location H&L point to.

cstm (custom) is special. It is not an Altair instruction instead it is used to write custom data to bytes. It is represented in lowercase to differentiate it from actual altair instructions.