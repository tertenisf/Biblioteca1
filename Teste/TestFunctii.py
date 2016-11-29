from Operations.Operations import Cautare
def TestCautare():
    assert Cautare([1,2,3,4],4)==True
    assert Cautare([],1)==False
    assert Cautare([1,2,3,4],'x')==False
TestCautare()