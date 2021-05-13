# Bitslice

Verilog-like bitslicing for Python.

## Installation

Install the library from PyPI:
~~~
pip install bitslice
~~~

## Quickstart
Bitslice is designed to behave as an integer value as much as possible.
All operators defined on `int` should be supported.

Bitslice objects use indexing to emulate Verilog-style bit slicing.

~~~ python
from bitslice import Bitslice
value = Bitslice(5, size=4)

# Binary: 0b0101
print(value)
0x0005 (5)

# Select the lowest bit (index 0, right-most)
#
#   index:   3210
#   value: 0b0101
print(value[0])
0x0001 (1)

# Select bits 2 -> 1
# resulting in 0b10 == 2
print(value[2:1])
0x0002 (2)

# Set the upper bit
value[3] = 1
# 0b1101
print(value)
0x000D (13)
~~~

Advanced features: slice aliasing
~~~ python
value = Bitslice(5, size=4)
value.add_alias('lower', start=0, end=1)
value.add_alias('upper', start=2, end=3)

value['lower'] == value[1:0]
~~~
See [bitslice.py](https://github.com/zegervdv/bitslice/blob/master/bitslice/bitslice.py) for more examples.
