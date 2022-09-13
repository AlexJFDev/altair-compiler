"""
This module contains the boilerplate Instruction class
"""

class Instruction():
    """
    This is a boilerplate class for instructions.
    """
    def __init__(self):
        pass
    def get_instruction_type(self) -> str:
        """
        Method to obtain a string representing the type of instruction that an object is.
        I did this because methods to get the type of a class bother me.
        """
        return "instruction"
    def generate_bytes(self, arguments: "list[str]") -> bytes:
        """ Boilerplate Method """
        return b''
