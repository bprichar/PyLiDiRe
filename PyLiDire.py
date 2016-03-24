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

class FortranComplex:
    """
    Mimick the Fortran Complex type
    """
    pass

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
