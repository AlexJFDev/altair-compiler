""" This module contains the boilerplate Instruction class """

class Instruction():
    """
    This is a boilerplate class for instructions.
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
    def generate_bytes(self, arguments: "list[str]") -> bytes:
        """ Boilerplate Method """
        return b''
