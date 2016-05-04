# PyLiDiRe
Python emulation of Fortran's List-Directed Read functionality

See this [reference](https://docs.oracle.com/cd/E19957-01/805-4939/6j4m0vnc5/index.html) for
a description of how this is supposed to function.

Usage involves creating FortranAsciiReader object, and then using it to read
into objects which have a .assign method. For convenience the following classes
are provided which behave as expected:

 * FortranCharacter
 * FortranInteger
 * FortranReal
 * FortranComplex
 * FortranLogical

As example:

    reader = FortranAsciiReader('file.txt')
    s = FortranCharacter()
    i = FortranInteger()
    r = FortranReal()
    reader.read(s, i, r)
    print s, i, r

If the file contains the following line:

    'Hello', , 4.5

would result in the following:

    Hello None 4.5
