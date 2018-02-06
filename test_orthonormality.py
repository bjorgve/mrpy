from primitiveImplementation import *
from wavelets import *
#Define the overall presision
eps = 0.01


def test_isNormOne():
    val = normWavletScaleZero(1,1)
    if val < 1.0 + eps and val > 1.0 - eps:
        assert True
    else:
        assert False

def test_isOrthogonal():
    val = normWavletScaleZero(2,1)
    if val > -eps and val < eps:
        assert True
    else:
        assert False

def test_isOrthogonalwrtTranslation():
    val = normWavletScale(2,2, 2, 2,0,1)
    if val > -eps and val < eps:
        assert True
    else:
        assert False

def test_isOrthogonalwrtScale():
    val = normWavletScale(2,1, 2, 2,1,1)
    if val > -eps and val < eps:
        assert True
    else:
        assert False

def test_isNormOnewrtScale():
    val = normWavletScale(2,1,2,1,1,1)
    if val < 1.0 + eps and val > 1.0 - eps:
        assert True
    else:
        assert False

def test_isWaveletNormOne():
    x = np.arange(0,1,.0001)
    y = np.array([wavelet(3,float(x[i]))[0] for i in range(x.size)])
    val = np.trapz(y*y,dx=0.0001)
    if val < 1.0 + eps and val > 1.0 - eps:
        assert True
    else:
        assert False

def test_isWaveletOrthogonal():

    x = np.arange(0,1,.0001)
    y = np.array([wavelet(3,float(x[i]))[0] for i in range(x.size)])
    y2 = np.array([wavelet(3,float(x[i]))[1] for i in range(x.size)])
    val = np.trapz(y*y2,dx=0.0001)
    if val > - eps and val <  eps:
        assert True
    else:
        assert False
