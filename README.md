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

Bitslice adds the ability to extract or set one or more bits of the value:

~~~ python
from bitslice import Bitslice
value = Bitslice(5, size=4)
value[3:1] - 1
~~~

Advanced features: slice aliasing
~~~ python
value = Bitslice(5, size=4)
value.add_alias('lower', start=0, end=1)
value.add_alias('upper', start=2, end=3)

value['lower'] == value[1:0]
~~~
See [bitslice.py](https://github.com/zegervdv/bitslice/blob/master/bitslice/bitslice.py) for more examples.
