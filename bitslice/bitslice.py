""" Bitslice
    VHDL/Verilog-like bit slicing of integer values.
"""


class Bitslice:
    """ A Bitslice can be created with a value:
        >>> Bitslice(7)
        0x0007 (7)

        Optionally with a predefined size:
        >>> Bitslice(7, size=4)
        0x0007 (7)

        Creating a Bitslice with a value larger than what can represented
        in the given size results in an error:
        >>> Bitslice(7, size=2)
        Traceback (most recent call last):
        ...
        ValueError: A value of 7 cannot be represented in 2 bits


        Bitslices allow slicing of sub-values from the value.
        >>> val = Bitslice(0xCAFEBABE)
        >>> val[7:0]
        0x00BE (190)
    """

    def __init__(self, value: int, size: int = None):
        self.value = value
        self.size = size

        if size is not None and value > (1 << size):
            raise ValueError(f"A value of {value} cannot be represented in {size} bits")

    def __repr__(self):
        return f"0x{self.value:04X} ({self.value})"

    def __getitem__(self, key):
        if isinstance(key, slice):
            mask = ((1 << (key.start - key.stop) + 1) - 1) << key.stop
            return Bitslice(
                (self.value & mask) >> key.stop, size=(key.start - key.stop) + 1
            )
