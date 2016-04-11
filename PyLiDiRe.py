"""
Python emulation of Fortran's List-Directed Read functionality
"""

import math

class FortranAsciiReader(file):

    def __init__(self, name):
        self._filename = name

    def read(self, *args):
        """
        Read from file into the given objects
        """
        # Read in line
        # Tokenize line into a list
            # Split on ',' and whitespace, handling quoted strings, and repetition
            # Assign elements one-by-one into args, skipping empty fields and stopping at a '/'
            # If line contained '/' or read into all varialbes, return
            # else, read in next line and continue tokenizing/assigning
        pass

class FortranCharacter:
    """
    Mimick the Fortran Character type
    """

    def __init__(self, value=None):
        if value is not None:
            self._value = str(value)
        else:
            self._value = None

    def __eq__(self, other):
        return other == self._value

    def __ne__(self, other):
        return other != self._value

    def __add__(self, other):
        return self._value + other

    def __radd__(self, other):
        return other + self._value

    def __iadd__(self, other):
        return self._value + other

    def __int__(self):
        return int(self._value)

    def __long__(self):
        return long(self._value)

    def __float__(self):
        return float(self._value)

    def __complex__(self):
        return complex(self._value)

    def __hex__(self):
        return hex(self._value)

    def __index__(self):
        return int(self._value)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return repr(self._value)

    def assign(self, value):
        self._value = str(value)

class FortranInteger:
    """
    Mimick the Fortran Integer type
    """

    def __init__(self, value=None):
        if value is not None:
            self._value = int(value)
        else:
            self._value = None

    def __eq__(self, other):
        return other == self._value

    def __ne__(self, other):
        return other != self._value

    def __lt__(self, other):
        return other > self._value

    def __gt__(self, other):
        return other < self._value

    def __le__(self, other):
        return other >= self._value

    def __ge__(self, other):
        return other <= self._value

    def __pos__(self):
        return +self._value

    def __neg__(self):
        return -self._value

    def __abs__(self):
        return abs(self._value)

    def __invert__(self):
        return ~self._value

    def __round__(self, n):
        return round(self._value, n)

    def __floor__(self):
        return math.floor(self._value)

    def __ceil__(self):
        return math.ceil(self._value)

    def __trunc__(self):
        return math.trunc(self._value)

    def __add__(self, other):
        return self._value + other

    def __sub__(self, other):
        return self._value - other

    def __mul__(self, other):
        return self._value * other

    def __floordiv__(self, other):
        return self._value // other

    def __div__(self, other):
        return self._value / other

    def __mod__(self, other):
        return self._value % other

    def __divmod__(self, other):
        return divmod(self._value, other)

    def __pow__(self, other):
        return self._value ** other

    def __lshift__(self, other):
        return self._value << other

    def __rshift__(self, other):
        return self._value >> other

    def __and__(self, other):
        return self._value & other

    def __or__(self, other):
        return self._value | other

    def __xor__(self, other):
        return self._value ^ other

    def __radd__(self, other):
        return other + self._value

    def __rsub__(self, other):
        return other - self._value

    def __rmul__(self, other):
        return other * self._value

    def __rfloordiv__(self, other):
        return other // self._value

    def __rdiv__(self, other):
        return other / self._value

    def __rmod__(self, other):
        return other % self._value

    def __rdivmod__(self, other):
        return divmod(other, self._value)

    def __rpow__(self, other):
        return other ** self._value

    def __rlshift__(self, other):
        return other << self._value

    def __rrshift__(self, other):
        return other >> self._value

    def __rand__(self, other):
        return other & self._value

    def __ror__(self, other):
        return other | self._value

    def __rxor__(self, other):
        return other ^ self._value

    def __iadd__(self, other):
        return self._value + other

    def __isub__(self, other):
        return self._value - other

    def __imul__(self, other):
        return self._value * other

    def __ifloordiv__(self, other):
        return self._value // other

    def __idiv__(self, other):
        return self._value / other

    def __imod__(self, other):
        return self._value % other

    def __ipow__(self, other):
        return self._value ** other

    def __ilshift__(self, other):
        return self._value << other

    def __irshift__(self, other):
        return self._value >> other

    def __iand__(self, other):
        return self._value & other

    def __ior__(self, other):
        return self._value | other

    def __ixor__(self, other):
        return self._value ^ other

    def __int__(self):
        return int(self._value)

    def __long__(self):
        return long(self._value)

    def __float__(self):
        return float(self._value)

    def __complex__(self):
        return complex(self._value)

    def __hex__(self):
        return hex(self._value)

    def __index__(self):
        return int(self._value)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return repr(self._value)

    def __format__(self, formatstr):
        return self._value.__format__(formatstr)

    def assign(self, value):
        self._value = int(value)

class FortranReal:
    """
    Mimick the Fortran Real type
    """

    def __init__(self, value=None):
        if value is not None:
            self._value = float(value)
        else:
            self._value = None

    def __eq__(self, other):
        return other == self._value

    def __ne__(self, other):
        return other != self._value

    def __lt__(self, other):
        return other > self._value

    def __gt__(self, other):
        return other < self._value

    def __le__(self, other):
        return other >= self._value

    def __ge__(self, other):
        return other <= self._value

    def __pos__(self):
        return +self._value

    def __neg__(self):
        return -self._value

    def __abs__(self):
        return abs(self._value)

    def __invert__(self):
        return ~self._value

    def __round__(self, n):
        return round(self._value, n)

    def __floor__(self):
        return math.floor(self._value)

    def __ceil__(self):
        return math.ceil(self._value)

    def __trunc__(self):
        return math.trunc(self._value)

    def __add__(self, other):
        return self._value + other

    def __sub__(self, other):
        return self._value - other

    def __mul__(self, other):
        return self._value * other

    def __floordiv__(self, other):
        return self._value // other

    def __div__(self, other):
        return self._value / other

    def __mod__(self, other):
        return self._value % other

    def __divmod__(self, other):
        return divmod(self._value, other)

    def __pow__(self, other):
        return self._value ** other

    def __lshift__(self, other):
        return self._value << other

    def __rshift__(self, other):
        return self._value >> other

    def __and__(self, other):
        return self._value & other

    def __or__(self, other):
        return self._value | other

    def __xor__(self, other):
        return self._value ^ other

    def __radd__(self, other):
        return other + self._value

    def __rsub__(self, other):
        return other - self._value

    def __rmul__(self, other):
        return other * self._value

    def __rfloordiv__(self, other):
        return other // self._value

    def __rdiv__(self, other):
        return other / self._value

    def __rmod__(self, other):
        return other % self._value

    def __rdivmod__(self, other):
        return divmod(other, self._value)

    def __rpow__(self, other):
        return other ** self._value

    def __rlshift__(self, other):
        return other << self._value

    def __rrshift__(self, other):
        return other >> self._value

    def __rand__(self, other):
        return other & self._value

    def __ror__(self, other):
        return other | self._value

    def __rxor__(self, other):
        return other ^ self._value

    def __iadd__(self, other):
        return self._value + other

    def __isub__(self, other):
        return self._value - other

    def __imul__(self, other):
        return self._value * other

    def __ifloordiv__(self, other):
        return self._value // other

    def __idiv__(self, other):
        return self._value / other

    def __imod__(self, other):
        return self._value % other

    def __ipow__(self, other):
        return self._value ** other

    def __ilshift__(self, other):
        return self._value << other

    def __irshift__(self, other):
        return self._value >> other

    def __iand__(self, other):
        return self._value & other

    def __ior__(self, other):
        return self._value | other

    def __ixor__(self, other):
        return self._value ^ other

    def __int__(self):
        return int(self._value)

    def __long__(self):
        return long(self._value)

    def __float__(self):
        return float(self._value)

    def __complex__(self):
        return complex(self._value)

    def __hex__(self):
        return hex(self._value)

    def __index__(self):
        return int(self._value)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return repr(self._value)

    def __format__(self, formatstr):
        return self._value.__format__(formatstr)

    def assign(self, value):
        self._value = float(value)

class FortranComplex:
    """
    Mimick the Fortran Complex type
    """

    def __init__(self, value=None):
        if value is not None:
            self._value = complex(value)
        else:
            self._value = None

    def __eq__(self, other):
        return other == self._value

    def __ne__(self, other):
        return other != self._value

    def __lt__(self, other):
        return other > self._value

    def __gt__(self, other):
        return other < self._value

    def __le__(self, other):
        return other >= self._value

    def __ge__(self, other):
        return other <= self._value

    def __pos__(self):
        return +self._value

    def __neg__(self):
        return -self._value

    def __abs__(self):
        return abs(self._value)

    def __invert__(self):
        return ~self._value

    def __round__(self, n):
        return round(self._value, n)

    def __floor__(self):
        return math.floor(self._value)

    def __ceil__(self):
        return math.ceil(self._value)

    def __trunc__(self):
        return math.trunc(self._value)

    def __add__(self, other):
        return self._value + other

    def __sub__(self, other):
        return self._value - other

    def __mul__(self, other):
        return self._value * other

    def __floordiv__(self, other):
        return self._value // other

    def __div__(self, other):
        return self._value / other

    def __mod__(self, other):
        return self._value % other

    def __divmod__(self, other):
        return divmod(self._value, other)

    def __pow__(self, other):
        return self._value ** other

    def __lshift__(self, other):
        return self._value << other

    def __rshift__(self, other):
        return self._value >> other

    def __and__(self, other):
        return self._value & other

    def __or__(self, other):
        return self._value | other

    def __xor__(self, other):
        return self._value ^ other

    def __radd__(self, other):
        return other + self._value

    def __rsub__(self, other):
        return other - self._value

    def __rmul__(self, other):
        return other * self._value

    def __rfloordiv__(self, other):
        return other // self._value

    def __rdiv__(self, other):
        return other / self._value

    def __rmod__(self, other):
        return other % self._value

    def __rdivmod__(self, other):
        return divmod(other, self._value)

    def __rpow__(self, other):
        return other ** self._value

    def __rlshift__(self, other):
        return other << self._value

    def __rrshift__(self, other):
        return other >> self._value

    def __rand__(self, other):
        return other & self._value

    def __ror__(self, other):
        return other | self._value

    def __rxor__(self, other):
        return other ^ self._value

    def __iadd__(self, other):
        return self._value + other

    def __isub__(self, other):
        return self._value - other

    def __imul__(self, other):
        return self._value * other

    def __ifloordiv__(self, other):
        return self._value // other

    def __idiv__(self, other):
        return self._value / other

    def __imod__(self, other):
        return self._value % other

    def __ipow__(self, other):
        return self._value ** other

    def __ilshift__(self, other):
        return self._value << other

    def __irshift__(self, other):
        return self._value >> other

    def __iand__(self, other):
        return self._value & other

    def __ior__(self, other):
        return self._value | other

    def __ixor__(self, other):
        return self._value ^ other

    def __int__(self):
        return int(self._value)

    def __long__(self):
        return long(self._value)

    def __float__(self):
        return float(self._value)

    def __complex__(self):
        return complex(self._value)

    def __hex__(self):
        return hex(self._value)

    def __index__(self):
        return int(self._value)

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return repr(self._value)

    def __format__(self, formatstr):
        return self._value.__format__(formatstr)

    def assign(self, value):
        self._value = complex(value)

class FortranLogical:
    """
    Mimick the Fortran Logical type
    """
    pass

def tokenize(line):
    """
    Tokenize the given line according to Fortran
    list-directed read rules.
    """
    pass
