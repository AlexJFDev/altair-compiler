"""
This class contains the MOVInstruction class
"""

from instruction import Instruction

class MOVInstruction(Instruction):
    """
    This class is for the MOV instruction which has special behavior for its bytecodes
    """

    SINGLE_REGISTER_DICTIONARY: "dict[str, int]" = {
        "b" : 0b000,
        "c" : 0b001,
        "d" : 0b010,
        "e" : 0b011,
        "h" : 0b100,
        "l" : 0b101,
        "m" : 0b110,
        "a" : 0b111
    }

    def __init__(self):
        pass
    def get_instruction_type(self) -> str:
        return "MOVInstruction"
    def generate_bytes(self, arguments: "list[str]") -> bytes:
        destination_register = self.SINGLE_REGISTER_DICTIONARY.get(arguments[0])
        source_register = self.SINGLE_REGISTER_DICTIONARY.get(arguments[1])
        byte_code = (0b01000000 + destination_register * 8 + source_register).to_bytes(1, "little")
        return byte_code
