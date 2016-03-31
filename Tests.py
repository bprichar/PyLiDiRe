import PyLiDiRe
import tempfile
import os

class ReaderTester:

    default_values = ["String", 42, 123.45, True]
    default_vars = [PyLiDiRe.FortranCharacter(),
                    PyLiDiRe.FortranInteger(),
                    PyLiDiRe.FortranReal(),
                    PyLiDiRe.FortranLogical()]

    def test_simple_read(self):
        for value, var in zip(default_values, default_vars):
            yield read_write, value, var

def read_write(val, var):
    f, n = tempfile.mkstemp(text=True)
    f.write(str(val))
    f.close()
    reader = FortranAsciiReader(n)
    reader.read(var)
    reader.close()
    os.remove(n)
    assert var == val
