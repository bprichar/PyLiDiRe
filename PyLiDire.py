"""
Python emulation of Fortran's List-Directed Read functionality
"""

class FortranAsciiReader(file):

    def __init__(self, name):
        self._filename = name

    def read(self, *args):
        """
        Read from file into the given objects
        """
        pass

class FortranCharacter:
    """
    Mimick the Fortran Character type
    """
    pass

class FortranInteger:
    """
    Mimick the Fortran Integer type
    """
    pass

class FortranReal:
    """
    Mimick the Fortran Real type
    """
    pass
