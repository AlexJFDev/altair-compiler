import sys;

try:
    file_location = sys.argv[1]
except:
    print("A file location was not passed as an argument.")
    print("Stopping compiler.")
    quit()

class Instruction():
    def __init__(self, _byte_code):
        self.byte_code = _byte_code
    def getInstructionType(self):
        return "simpleinstruction"

class SimpleInstruction(Instruction):
    def __init__(self, _byte_code):
        self.byte_code = _byte_code
    def getInstructionType(self):
        return "simpleinstruction"
    def getByteCode(self):
        return self.byte_code

class SimpleArgumentInstruction(SimpleInstruction):
    def __init__(self, _byte_code, _number_of_arguments):
        self.byte_code = _byte_code
        self.number_of_arguments = _number_of_arguments
    def getInstructionType(self):
        return "simpleargumentinstruction"
    def getNumberOfArguments(self):
        return self.number_of_arguments

class inByteArgument(Instruction):
    def __init__(self, _front_bits, _end_bits = 0):
        self.front_bits = _front_bits
        self.end_bits = _end_bits
    def getInstructionType(self):
        return "inbyteargument"

class customByte(Instruction):
    def __init__(self):
        pass

class moveInstruction(Instruction):
    def __init__(self):
        pass
    def getInstructionType(self):
        return "moveinstruction"
        
instruction_dictionary = {
    ###### Command Instructions
    ### Input/Output Instructions
    "IN" : SimpleArgumentInstruction(b'\xdb', 1),
    "OUT" : SimpleArgumentInstruction(b'\xd3', 1),
    ### Interupt Instructions
    "EI" : SimpleInstruction(b'\xfb'),
    "DI" : SimpleInstruction(b'\xf3'),
    "HLT" : SimpleInstruction(b'\x76'),
    #RST
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
    "MOV" : moveInstruction(),
    #STAX
    #LDAX
    ### Register/Memory to Accumulator Transfers
    #ADD
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
    #JMP
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
    print(line)
    if line[0] == "#":
        continue
    line = line.replace("\n","")
    line_split = line.split(",")
    instruction_string = line_split[0]
    instruction = instruction_dictionary.get(instruction_string)
    instruction_type = instruction.getInstructionType()
    if instruction_type == "simpleinstruction":
        byte_code = instruction.getByteCode()
        compiled_bytes += byte_code
    elif instruction_type == "simpleargumentinstruction":
        byte_code = instruction.getByteCode()
        compiled_bytes += byte_code
        for argument in range(1, instruction.getNumberOfArguments() + 1):
            argument_byte = line_split[argument]
            compiled_bytes += bytes.fromhex(argument_byte)
    elif instruction_type == "moveinstruction":
        destination_register = single_register_dictionary.get(line_split[1])
        source_register = single_register_dictionary.get(line_split[2])
        byte_code = (0b01000000 + destination_register * 8 + source_register).to_bytes(1, "little")
        compiled_bytes += byte_code

print(compiled_bytes)
file_location = file_location[:file_location.rfind(".")]
with open(f"{file_location}.bin", "wb") as output_file:
    output_file.write(compiled_bytes)