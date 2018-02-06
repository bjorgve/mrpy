from scaling import *
import numpy as np
def ftest(x):
    return np.sin(2.0*np.pi*x)


eps = 10**-3
def test_scalingCoef():
    val1 =scalingCoef(2,4,2,0,ftest)
    val2 = approximatedScalingCoef(2,2,0,ftest)
    print(np.abs(val1-val2))
    if np.abs(val1-val2) < eps:
        assert True
    else:
        assert False
