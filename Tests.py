import PyLiDiRe

def test_read_just_string():
    reader = PyLiDiRe.FortranAsciiReader('string.txt')
    var = PyLiDiRe.FortranCharacter()
    reader.read(var)
    assert var == 'String'

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
