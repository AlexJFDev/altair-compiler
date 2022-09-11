""" This module contains the ComplexInstruction class """

from instruction import Instruction

class ComplexInstruction(Instruction):
    """
    This is a class for complex instructions that don't
    always have the same bytecode and might have arguments.
    """
    def __init__(self, _front_bits, _end_bits = "na", _number_of_arguments = 0):
        self.front_bits = _front_bits
        self.end_bits = _end_bits
        self.number_of_arguments = _number_of_arguments
    def get_front_bits(self):
        """ boilerplate """
        return self.front_bits
    def get_end_bits(self):
        """ boilerplate """
        return self.end_bits
    def get_number_of_arguments(self):
        """ boilerplate """
        return self.number_of_arguments
    def get_instruction_type(self):
        return "complexInstruction"
