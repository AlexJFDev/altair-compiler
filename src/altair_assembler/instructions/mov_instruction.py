""" This class contains the MOVInstruction class """

from .instruction import Instruction

class MOVInstruction(Instruction):
    """
    This class is for the MOV instruction which has special behavior for its bytecodes
    """

    def __init__(self):
        pass
    def generate_bytes(self, arguments: "list[str]") -> bytes:
        destination_register = self.SINGLE_REGISTER_DICTIONARY.get(arguments[0])
        source_register = self.SINGLE_REGISTER_DICTIONARY.get(arguments[1])
        byte_code = (0b01000000 + destination_register * 8 + source_register).to_bytes(1, "little")
        return byte_code
