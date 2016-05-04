import PyLiDiRe

def test_read_just_string():
    reader = PyLiDiRe.FortranAsciiReader('string.txt')
    var = PyLiDiRe.FortranCharacter()
    reader.read(var)
    assert var == 'String'

def test_read_just_quoted_string():
    reader = PyLiDiRe.FortranAsciiReader('quoted_string.txt')
    var = PyLiDiRe.FortranCharacter()
    reader.read(var)
    assert var == 'Things'

def test_read_just_integer():
    reader = PyLiDiRe.FortranAsciiReader('integer.txt')
    var = PyLiDiRe.FortranInteger()
    reader.read(var)
    assert var == 42

def test_read_just_float():
    reader = PyLiDiRe.FortranAsciiReader('float.txt')
    var = PyLiDiRe.FortranReal()
    reader.read(var)
    assert var == 11.7

def test_read_just_complex():
    reader = PyLiDiRe.FortranAsciiReader('complex.txt')
    var = PyLiDiRe.FortranComplex()
    reader.read(var)
    assert var == complex(1.2,3.4)

def test_read_multiple():
    reader = PyLiDiRe.FortranAsciiReader('multiple.txt')
    cvar = PyLiDiRe.FortranCharacter()
    fvar = PyLiDiRe.FortranReal()
    ivar = PyLiDiRe.FortranInteger()
    reader.read(cvar, fvar, ivar)
    assert cvar == 'Yep'
    assert fvar == 12.34
    assert ivar == 56

def test_read_complicated():
    reader = PyLiDiRe.FortranAsciiReader('complicated.txt')
    cvar1 = PyLiDiRe.FortranComplex()
    cvar2 = PyLiDiRe.FortranComplex()
    cvar3 = PyLiDiRe.FortranComplex()
    cvar4 = PyLiDiRe.FortranComplex()
    svar1 = PyLiDiRe.FortranCharacter()
    svar2 = PyLiDiRe.FortranCharacter()
    svar3 = PyLiDiRe.FortranCharacter()
    svar4 = PyLiDiRe.FortranCharacter()
    svar5 = PyLiDiRe.FortranCharacter()
    svar6 = PyLiDiRe.FortranCharacter()
    reader.read(cvar1, cvar2, cvar3, cvar4, svar1, svar2, svar3, svar4, svar5, svar6)
    assert cvar1 == complex(3.,2.)
    assert cvar2 == complex(3.,2.)
    assert cvar3 == complex(3.,2.)
    assert cvar4 == complex(3.,2.)
    assert svar1 == None
    assert svar2 == None
    assert svar3 == 'hello'
    assert svar4 == 'hello'
    assert svar5 == 'hello'
    assert svar6 == 'hello'

def test_read_multiline():
    reader = PyLiDiRe.FortranAsciiReader('multiline.txt')
    var1 = PyLiDiRe.FortranCharacter()
    var2 = PyLiDiRe.FortranCharacter()
    var3 = PyLiDiRe.FortranCharacter()
    var4 = PyLiDiRe.FortranCharacter()
    reader.read(var1, var2, var3, var4)
    assert var1 == 'Hello'
    assert var2 == 'World'
    assert var3 == 'Tada'
    assert var4 == None
