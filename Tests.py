import PyLiDiRe
import tempfile
import os

default_values = ["String", 42, 123.45, True]
default_vars = [PyLiDiRe.FortranCharacter(),
                PyLiDiRe.FortranInteger(),
                PyLiDiRe.FortranReal(),
                PyLiDiRe.FortranLogical()]

def test_simple_read():
        for value, var in zip(default_values, default_vars):
            yield read_write, value, var

def read_write(val, var):
    fd, n = tempfile.mkstemp(text=True)
    os.close(fd)
    f = open(n, 'w')
    f.write(str(val))
    f.close()
    reader = PyLiDiRe.FortranAsciiReader(n)
    reader.read(var)
    reader.close()
    os.remove(n)
    assert var == val
