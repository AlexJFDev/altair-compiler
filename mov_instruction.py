"""
This class contains the MOVInstruction class
"""

from instruction import Instruction

class MOVInstruction(Instruction):
    """
    This class is for the MOV instruction which has special behavior for its bytecodes
    """
    def __init__(self):
        pass
    def get_instruction_type(self):
        return "MOVInstruction"