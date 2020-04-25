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

        Get the size of a Bitslice:
        >>> val = Bitslice(4, size=8)
        >>> len(val)
        8

        For undetermined sizes, the minimal number of bits needed is used
        >>> val = Bitslice(4)
        >>> len(val)
        3


        Bitslices allow slicing of sub-values from the value.
        >>> val = Bitslice(0xCAFEBABE)
        >>> val[7:0]
        0x00BE (190)

        Or a single bit:
        >>> val[3]
        0x0001 (1)

        Assign new values to bits or slices:
        >>> val[3] = 0
        >>> val
        0xCAFEBAB6 (3405691574)
        >>> val[7:0] = 4
        >>> val
        0xCAFEBA04 (3405691396)
    """

    def __init__(self, value: int, size: int = None):
        self.value = value
        self.size = size

        if size is not None and value > (1 << size):
            raise ValueError(f"A value of {value} cannot be represented in {size} bits")

    def __repr__(self):
        return f"0x{self.value:04X} ({self.value})"

    def __len__(self):
        if self.size is not None:
            return self.size
        else:
            return self.value.bit_length()

    def _mask_shift_size(self, key):
        if isinstance(key, slice):
            mask = ((1 << (key.start - key.stop) + 1) - 1) << key.stop
            size = (key.start - key.stop) + 1
            shift = key.stop
        elif isinstance(key, int):
            mask = 1 << key
            size = 1
            shift = key
        return mask, shift, size

    def __getitem__(self, key):
        mask, shift, size = self._mask_shift_size(key)
        return Bitslice((self.value & mask) >> shift, size=size)

    def __setitem__(self, key, value):
        mask, shift, size = self._mask_shift_size(key)
        mask_value = self.value & (mask ^ ((1 << len(self)) - 1))
        self.value = mask_value | (value << shift) & mask
