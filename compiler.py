import sys;

try:
    file_location = sys.argv[1]
except:
    print("A file location was not passed as an argument.")
    print("Stopping compiler.")
    quit()
class Instruction:
    def __init__(self, _byte_code):
        self.byte_code = _byte_code
    def getInstructionType(self):
        return "instruction"
    def getByteCode(self):
        return self.byte_code

class SimpleInstruction(Instruction):
    def __init__(self, _byte_code):
        self.byte_code = _byte_code
    def getInstructionType(self):
        return "simpleinstruction"

class SimpleArgumentInstruction(Instruction):
    def __init__(self, _byte_code, _number_of_arguments):
        self.byte_code = _byte_code
        self.number_of_arguments = _number_of_arguments
    def getInstructionType(self):
        return "simpleargumentinstruction"
    def getNumberOfArguments(self):
        return self.number_of_arguments

class inByteTwoArgumentInstruction(Instruction):
    def __init__(self, _byte_code, _number_of_arguments):
        self.byte_code = _byte_code
        self.number_of_arguments = _number_of_arguments
    def getInstructionType(self):
        return "inbytetwoargumentinstruction"
        
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
    #MOV
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
    byte_code = instruction.getByteCode()
    if instruction_type == "simpleinstruction":
        compiled_bytes = compiled_bytes + byte_code
    elif instruction_type == "simpleargumentinstruction":
        compiled_bytes = compiled_bytes + byte_code
        for argument in range(1, instruction.getNumberOfArguments() + 1):
            argument_byte = line_split[argument]
            compiled_bytes = compiled_bytes + bytes.fromhex(argument_byte)
    elif instruction_type == "":
        pass

print(compiled_bytes)
file_location = file_location[:file_location.rfind(".")]
with open(f"{file_location}.bin", "wb") as output_file:
    output_file.write(compiled_bytes)