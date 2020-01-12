from ui import *
from model import *

def test_add():
    complexi = createComplex(1,2)
    assert(getReal(complexi)==1)
    setReal(complexi,1)
    setImaginary(complexi,3)
    assert(getImaginary(complexi)==3)

def run_tests():
    test_add()
