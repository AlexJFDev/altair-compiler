""" This module contains the ComplexInstruction class """

from .instruction import Instruction

class ComplexInstruction(Instruction):
    """
    This is a class for complex instructions that don't
    always have the same bytecode and might have arguments.
    """
    def __init__(self, _front_bits : str, _end_bits : str = None, _number_of_arguments : int = 0):
        self.front_bits: str = _front_bits
        self.end_bits: str = _end_bits
        self.number_of_arguments: int = _number_of_arguments
    def generate_bytes(self, arguments: "list[str]") -> bytes:
        argument_bits: str = arguments[0]
        front_bits_length: int = len(self.front_bits)
        argument_bits_length: int = len(argument_bits)
        front_int: int = int(self.front_bits, 2) * pow(2, 8 - front_bits_length)
        argument_int: int = int(argument_bits, 2) * pow(2, 8 - front_bits_length - argument_bits_length)
        if self.end_bits is None:
            byte_code: bytes = (front_int + argument_int).to_bytes(1, "little")
        else:
            end_int: int = int(self.end_bits, 2)
            byte_code: bytes = (front_int + argument_int + end_int).to_bytes(1, "little")
        return_bytes: bytes = byte_code
        for argument_number in range(1, self.number_of_arguments):
            argument: str = arguments[argument_number]
            return_bytes += bytes.fromhex(argument)
        return return_bytes
