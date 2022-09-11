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
    def get_instruction_type(self):
        return "customByte"
