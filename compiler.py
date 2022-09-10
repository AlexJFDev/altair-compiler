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
    def __init__(self, _byte_code):
        self.byte_code = _byte_code
    def getInstructionType(self):
        return "simpleInstruction"
    def getByteCode(self):
        return self.byte_code

class SimpleArgumentInstruction(SimpleInstruction):
    def __init__(self, _byte_code, _number_of_arguments):
        self.byte_code = _byte_code
        self.number_of_arguments = _number_of_arguments
    def getInstructionType(self):
        return "simpleArgumentInstruction"
    def getNumberOfArguments(self):
        return self.number_of_arguments

class InByteArgumentInstruction(Instruction):
    def __init__(self, _front_bits, _end_bits = "na"):
        self.front_bits = _front_bits
        self.end_bits = _end_bits
    def getInstructionType(self):
        return "inByteArgumentInstruction"
    def getFrontBits(self):
        return self.front_bits
    def getEndBits(self):
        return self.end_bits

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
    "IN" : SimpleArgumentInstruction(b'\xdb', 1),
    "OUT" : SimpleArgumentInstruction(b'\xd3', 1),
    ### Interrupt Instructions
    "EI" : SimpleInstruction(b'\xfb'),
    "DI" : SimpleInstruction(b'\xf3'),
    "HLT" : SimpleInstruction(b'\x76'),
    "RST" : InByteArgumentInstruction("11", _end_bits = "111"),
    ### Carry Bit Instructions
    "CMC" : SimpleInstruction(b'\x3f'),
    "STC" : SimpleInstruction(b'\x37'),
    ### No Operation Instruction
    "NOP" : SimpleInstruction(b'\x00'),
    ###### Single Register Instructions
    #INR
    #DCR
    "CMA" : SimpleInstruction(b'\x2f'),
    "DAA" : SimpleInstruction(b'\x27'),
    ###### Register Pair Instructions
    #PUSH
    #POP
    #DAD
    #INX
    "INX" : InByteArgumentInstruction("00", _end_bits = "0011"),
    #DCX
    "XCHG" : SimpleInstruction(b'\xeb'),
    "XTHL" : SimpleInstruction(b'\xe3'),
    ###### Rotate Accumulator Instructions
    "RLC" : SimpleInstruction(b'\x07'),
    "RRC" : SimpleInstruction(b'\x0f'),
    "RAL" : SimpleInstruction(b'\x17'),
    "RAR" : SimpleInstruction(b'\x1f'),
    ###### Data Transfer Instructions
    ### Data Transfer Instructions
    "MOV" : MoveInstruction(),
    #STAX
    #LDAX
    ### Register/Memory to Accumulator Transfers
    "ADD" : InByteArgumentInstruction("10000"),
    #ADC
    #SUB
    #SBB
    #ANA
    #XRA
    #ORA
    #CMP
    ### Direct Addressing Instructions
    "STA" : SimpleArgumentInstruction(b'\x32', 2),
    "LDA" : SimpleArgumentInstruction(b'\x3a', 2),
    "SHLD" : SimpleArgumentInstruction(b'\x22', 2),
    "LHLD" : SimpleArgumentInstruction(b'\x2a', 2),
    ###### Immediate Instructions
    #LXI
    #MVI
    #ADI
    #ACI
    #SUI
    #SBI
    #ANI
    #XRI
    #ORI
    #CPI
    ###### Branching Instructions
    ### Jump Instructions
    #PCHL
    "JMP" : SimpleArgumentInstruction(b'\xc3', 2),
    #JC
    #JNC
    #JZ
    #JNZ
    #JM
    #JP
    #JPE
    #JPO
    ### Call Instructions
    #CALL
    #CC
    #CNC
    #CZ
    #CNZ
    #CM
    #CP
    #CPE
    #CPO
    ### Return Instructions
    #RET
    #RC
    #RNC
    #RZ
    #RNZ
    #RM
    #RP
    #RPE
    #RPO


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
compiled_bytes = b''

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

    elif instruction_type == "simpleArgumentInstruction":
        byte_code = instruction.getByteCode()
        compiled_bytes += byte_code
        for argument in range(1, instruction.getNumberOfArguments() + 1):
            argument_byte = line_split[argument]
            compiled_bytes += bytes.fromhex(argument_byte)

    elif instruction_type == "inByteArgumentInstruction":
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