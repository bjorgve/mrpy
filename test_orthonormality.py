from primitiveImplementation import *

eps = 0.01

def test_IsNormOne():
    val = normWavletScaleZero(1,1)
    if val < 1.0 + eps and val > 1.0 - eps:
        assert True
    else:
        assert False

def test_IsOrthogonal():
    val = normWavletScaleZero(2,1)
    if val > -eps and val < eps:
        assert True
    else:
        assert False

def test_IsOrthogonalwrtTranslation():
    val = normWavletScale(2,2, 2, 2,0,1)
    if val > -eps and val < eps:
        assert True
    else:
        assert False

def test_IsOrthogonalwrtScale():
    val = normWavletScale(2,1, 2, 2,1,1)
    if val > -eps and val < eps:
        assert True
    else:
        assert False

def test_IsNormOnewrtScale():
    val = normWavletScale(2,1,2,1,1,1)
    if val < 1.0 + eps and val > 1.0 - eps:
        assert True
    else:
        assert False
