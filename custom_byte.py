"""
This module contains the CustomByte class
"""

from instruction import Instruction

class CustomByte(Instruction):
    """
    This class allows for special bytes meant to be used as data for a program.
    """
    def __init__(self):
        pass
    def get_instruction_type(self) -> str:
        return "customByte"
    def generate_bytes(self, arguments: "list[str]") -> bytes:
        return_bytes: bytes = b''
        for data_byte in arguments:
            print(data_byte)
            return_bytes += bytes.fromhex(data_byte)
        return return_bytes
