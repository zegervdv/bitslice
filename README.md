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

See [bitslice.py](https://github.com/zegervdv/bitslice/blob/master/bitslice/bitslice.py) for more examples.
