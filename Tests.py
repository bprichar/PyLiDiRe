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
