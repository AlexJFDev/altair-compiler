import sys;

try:
    file_location = sys.argv[1]
except:
    print("a file location was not passed as an argument")
    print("STOPPING COMPILER")
    quit()

class Instruction():
    def __init__(self, _byte_code):
        self.byte_code = _byte_code
    def getInstructionType(self):
        return "instruction"

class SimpleInstruction(Instruction):
    def __init__(self, _byte_code, _number_of_arguments = 0):
        self.byte_code = _byte_code
        self.number_of_arguments = _number_of_arguments
    def getByteCode(self):
        return self.byte_code
    def getNumberOfArguments(self):
        return self.number_of_arguments
    def getInstructionType(self):
        return "simpleInstruction"

class ComplexInstruction(Instruction):
    def __init__(self, _front_bits, _end_bits = "na", _number_of_arguments = 0):
        self.front_bits = _front_bits
        self.end_bits = _end_bits
        self.number_of_arguments = _number_of_arguments
    def getFrontBits(self):
        return self.front_bits
    def getEndBits(self):
        return self.end_bits
    def getNumberOfArguments(self):
        return self.number_of_arguments
    def getInstructionType(self):
        return "complexInstruction"

class CustomByte(Instruction):
    def __init__(self):
        pass
    def getInstructionType(self):
        return "customByte"

class MoveInstruction(Instruction):
    def __init__(self):
        pass
    def getInstructionType(self):
        return "moveInstruction"
        
instruction_dictionary = {
    ###### Command Instructions
    ### Input/Output Instructions
    "IN" : SimpleInstruction(b"\xdb", _number_of_arguments = 1),
    "OUT" : SimpleInstruction(b"\xd3", _number_of_arguments = 1),
    ### Interrupt Instructions
    "EI" : SimpleInstruction(b"\xfb"),
    "DI" : SimpleInstruction(b"\xf3"),
    "HLT" : SimpleInstruction(b"\x76"),
    "RST" : ComplexInstruction("11", _end_bits = "111"),
    ### Carry Bit Instructions
    "CMC" : SimpleInstruction(b"\x3f"),
    "STC" : SimpleInstruction(b"\x37"),
    ### No Operation Instruction
    "NOP" : SimpleInstruction(b"\x00"),
    ###### Single Register Instructions
    "INR" : ComplexInstruction("00", _end_bits = "100"),
    "DCR" : ComplexInstruction("00", _end_bits = "101"),
    "CMA" : SimpleInstruction(b"\x2f"),
    "DAA" : SimpleInstruction(b"\x27"),
    ###### Register Pair Instructions
    "PUSH" : ComplexInstruction("11", _end_bits = "0101"),
    "POP" : ComplexInstruction("11", _end_bits = "0001"),
    "DAD" : ComplexInstruction("00", _end_bits = "1001"),
    "INX" : ComplexInstruction("00", _end_bits = "0011"),
    "DCX" : ComplexInstruction("00", _end_bits = "1011"),
    "XCHG" : SimpleInstruction(b"\xeb"),
    "XTHL" : SimpleInstruction(b"\xe3"),
    ###### Rotate Accumulator Instructions
    "RLC" : SimpleInstruction(b"\x07"),
    "RRC" : SimpleInstruction(b"\x0f"),
    "RAL" : SimpleInstruction(b"\x17"),
    "RAR" : SimpleInstruction(b"\x1f"),
    ###### Data Transfer Instructions
    ### Data Transfer Instructions
    "MOV" : MoveInstruction(),
    "STAX" : ComplexInstruction("000", _end_bits = "0010"),
    "LDAX" : ComplexInstruction("000", _end_bits = "1010"),
    ### Register/Memory to Accumulator Transfers
    "ADD" : ComplexInstruction("10000"),
    "ADC" : ComplexInstruction("10001"),
    "SUB" : ComplexInstruction("10010"),
    "SBB" : ComplexInstruction("10011"),
    "ANA" : ComplexInstruction("10100"),
    "XRA" : ComplexInstruction("10101"),
    "ORA" : ComplexInstruction("10110"),
    "CMP" : ComplexInstruction("10111"),
    ### Direct Addressing Instructions
    "STA" : SimpleInstruction(b"\x32", _number_of_arguments = 2),
    "LDA" : SimpleInstruction(b"\x3a", _number_of_arguments = 2),
    "SHLD" : SimpleInstruction(b"\x22", _number_of_arguments = 2),
    "LHLD" : SimpleInstruction(b"\x2a", _number_of_arguments = 2),
    ###### Immediate Instructions
    "LXI" : ComplexInstruction("00", _end_bits = "0001", _number_of_arguments = 1),
    "MVI" : ComplexInstruction("00", _end_bits = "110", _number_of_arguments = 2),
    "ADI" : SimpleInstruction(b"\xc6", _number_of_arguments = 1),
    "ACI" : SimpleInstruction(b"\xce", _number_of_arguments = 1),
    "SUI" : SimpleInstruction(b"\xd6", _number_of_arguments = 1),
    "SBI" : SimpleInstruction(b"\xde", _number_of_arguments = 1),
    "ANI" : SimpleInstruction(b"\xe6", _number_of_arguments = 1),
    "XRI" : SimpleInstruction(b"\xee", _number_of_arguments = 1),
    "ORI" : SimpleInstruction(b"\xf6", _number_of_arguments = 1),
    "CPI" : SimpleInstruction(b"\xfe", _number_of_arguments = 1),
    ###### Branching Instructions
    ### Jump Instructions
    "PCHL" : SimpleInstruction(b"\xe9"),
    "JMP" : SimpleInstruction(b"\xc3", _number_of_arguments = 2),
    "JC" : SimpleInstruction(b"\xda", _number_of_arguments = 2),
    "JNC" : SimpleInstruction(b"\xd2", _number_of_arguments = 2),
    "JZ" : SimpleInstruction(b"\xca", _number_of_arguments = 2),
    "JNZ" : SimpleInstruction(b"\xc2", _number_of_arguments = 2),
    "JM" : SimpleInstruction(b"\xfa", _number_of_arguments = 2),
    "JP" : SimpleInstruction(b"\xf2", _number_of_arguments = 2),
    "JPE" : SimpleInstruction(b"\xea", _number_of_arguments = 2),
    "JPO" : SimpleInstruction(b"\xe2", _number_of_arguments = 2),
    ### Call Instructions
    "CALL" : SimpleInstruction(b"\xcd", _number_of_arguments = 2),
    "CC" : SimpleInstruction(b"\xdc", _number_of_arguments = 2),
    "CNC" : SimpleInstruction(b"\xd4", _number_of_arguments = 2),
    "CZ" : SimpleInstruction(b"\xcc", _number_of_arguments = 2),
    "CNZ" : SimpleInstruction(b"\xc4", _number_of_arguments = 2),
    "CM" : SimpleInstruction(b"\xfc", _number_of_arguments = 2),
    "CP" : SimpleInstruction(b"\xf4", _number_of_arguments = 2),
    "CPE" : SimpleInstruction(b"\xec", _number_of_arguments = 2),
    "CPO" : SimpleInstruction(b"\xe4", _number_of_arguments = 2),
    ### Return Instructions
    "RET" : SimpleInstruction(b"\xc9"),
    "RC" : SimpleInstruction(b"\xd8"),
    "RNC" : SimpleInstruction(b"\xd0"),
    "RZ" : SimpleInstruction(b"\xc8"),
    "RNZ" : SimpleInstruction(b"\xc0"),
    "RM" : SimpleInstruction(b"\xf8"),
    "RP" : SimpleInstruction(b"\xf0"),
    "RPE" : SimpleInstruction(b"\xe8"),
    "RPO" : SimpleInstruction(b"\xe0"),

    ###### Custom Byte
    ### This is not an Altair instruction. It is for bytes to be placed at the end of a program that contain needed data.
    "CSTM" : CustomByte()
}

single_register_dictionary = {
    "b" : 0b000,
    "c" : 0b001,
    "d" : 0b010,
    "e" : 0b011,
    "h" : 0b100,
    "l" : 0b101,
    "m" : 0b110,
    "a" : 0b111
}

file = open(file_location, "r")
compiled_bytes = b""

for line in file:
    print(line[:-1])
    if line[0] == "#":
        continue
    line = line.replace("\n","")
    line_split = line.split(",")
    instruction_string = line_split[0]
    instruction = instruction_dictionary.get(instruction_string)
    try:
        instruction_type = instruction.getInstructionType()
    except AttributeError:
        print(f"the instruction {instruction_string} was not recognized")
        print("STOPPING COMPILER")
        quit()
    if instruction_type == "simpleInstruction":
        byte_code = instruction.getByteCode()
        compiled_bytes += byte_code
        for argument in range(1, instruction.getNumberOfArguments() + 1):
            argument_byte = line_split[argument]
            compiled_bytes += bytes.fromhex(argument_byte)

    elif instruction_type == "complexInstruction":
        front_bits = instruction.getFrontBits()
        end_bits = instruction.getEndBits()
        argument_bits = line_split[1]
        front_bits_length = len(front_bits)
        argument_bits_length = len(argument_bits)
        front_bits = int(front_bits, 2) * pow(2, 8 - front_bits_length)
        argument_bits = int(argument_bits, 2) * pow(2, 8 - front_bits_length - argument_bits_length)
        if end_bits == "na":
            byte_code = (front_bits + argument_bits).to_bytes(1, "little")
        else:
            end_bits = int(end_bits, 2)
            byte_code = (front_bits + argument_bits + end_bits).to_bytes(1, "little")
        compiled_bytes += byte_code
        for argument in range(1, instruction.getNumberOfArguments() + 1):
            argument_byte = line_split[argument]
            compiled_bytes += bytes.fromhex(argument_byte)

    elif instruction_type == "customByte":
        for data_byte in line_split[1:]:
            compiled_bytes += bytes.fromhex(data_byte)

    elif instruction_type == "moveInstruction":
        destination_register = single_register_dictionary.get(line_split[1])
        source_register = single_register_dictionary.get(line_split[2])
        byte_code = (0b01000000 + destination_register * 8 + source_register).to_bytes(1, "little")
        compiled_bytes += byte_code

print(compiled_bytes)
file_location = file_location[:file_location.rfind(".")]
with open(f"{file_location}.bin", "wb") as output_file:
    output_file.write(compiled_bytes)
print(f"writing compiled program to {file_location}.bin")
print("COMPLIER FINISHED SUCCESSFULLY")