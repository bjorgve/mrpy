from primitiveImplementation import *



def test_IsNormOne():
    val = normWavletScaleZero(1,1)
    if val < 1.01 and val > 0.09:
        assert True
    else:
        assert False

def test_IsOrthogonal():
    val = normWavletScaleZero(2,1)
    if val > -0.01 and val < 0.01:
        assert True
    else:
        assert False

def test_IsOrthogonalwrtTranslation():
    val = normWavletScale(2,2, 2, 2,0,1)
    if val > -0.01 and val < 0.01:
        assert True
    else:
        assert False

def test_IsOrthogonalwrtScale():
    val = normWavletScale(2,1, 2, 2,1,1)
    if val > -0.01 and val < 0.01:
        assert True
    else:
        assert False

def test_IsNormOnewrtScale():
    val = normWavletScale(2,1,2,1,1,1)
    if val < 1.01 and val > 0.09:
        assert True
    else:
        assert False    
