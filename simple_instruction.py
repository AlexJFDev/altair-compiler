"""
This module contains the SimpleInstruction class
"""

from instruction import Instruction

class SimpleInstruction(Instruction):
    """
    This is a class for simple instructions that
    always have the same bytecode and might have arguments.
    """
    def __init__(self, _byte_code: bytes, _number_of_arguments: int = 0):
        self.byte_code = _byte_code
        self.number_of_arguments = _number_of_arguments
    def get_byte_code(self) -> bytes:
        """
        boilerplate
        """
        return self.byte_code
    def get_number_of_arguments(self) -> int:
        """
        boilerplate
        """
        return self.number_of_arguments
    def get_instruction_type(self) -> str:
        return "simpleInstruction"
    def generate_bytes(self, arguments: "list[str]") -> bytes:
        return_bytes = self.byte_code
        for argument in arguments:
            return_bytes += bytes.fromhex(argument)
        return return_bytes