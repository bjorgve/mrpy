import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.legendre as leg


# Return the function value of the specified order
# of the legendre polynomial defined on the area [0,1]
def legendrePolynomial(order, x):
    coef = []
    if type(x) is float:

        if x <= 0 or x > 1:
            return 0
        else:
            for n in range(0, order + 1):
                if(n == order):
                    coef.append(1)
                else:
                    coef.append(0)
            return (2.*order + 1.)**.5 \
                * leg.Legendre(coef, domain=[-1, 1])(2.0*x - 1)
    else:
        y = np.zeros(x.size)

        for i in range(x.size):

            if x[i] <= 0 or x[i] > 1:
                y[i] = 0
            else:
                for n in range(0, order+1):
                    if(n == order):
                        coef.append(1)
                    else:
                        coef.append(0)

                y[i] = (2.*order + 1.)**.5 \
                    * leg.Legendre(coef, domain=[-1, 1])(2.0*x[i] - 1)
                coef.clear()
    return y


# Returns the function value of the scale and translated
# legendre polynomial
def scaling(order, scale, translation, x):
    return 2**(scale/2)*legendrePolynomial(order, 2**scale*x - translation)


def scalingVec(nr_poly, scale, translation, x):
    tmp = np.empty(nr_poly)
    for i in range(nr_poly):
        tmp[i] = scaling(i, scale, translation, x)
    return tmp


# Returns the roots of the legendre polynomial
def roots(order):
    coef = []
    for n in range(0, order+1):
        if n == order:
            coef.append(1)
        else:
            coef.append(0)
    return .5*(leg.legroots(coef) + 1)


# Returns the weights of the legendre polynomial defined on
def weights(order):

    x = roots(order)
    w = np.empty(order)
    coef = []
    for n in range(0, order+1):
        if(n == order):
            coef.append(1)
        else:
            coef.append(0)

    derivative_coefficients = leg.legder(coef)
    del coef[-1]
    del coef[-1]
    coef.append(1)
    for i in range(0, order):
        tmp = leg.Legendre(derivative_coefficients, domain=[-1, 1])(2*x[i] - 1)
        tmp2 = leg.Legendre(coef, domain=[-1, 1])(2.0*x[i] - 1)
        w[i] = 1/(order*tmp*tmp2)
        # Possibly some bug here, get a factor 2 different using mathematica
    return w


# Numerical approximation of the scaling functions
def np_scaling(order, f):
    x = np.arange(0, 1, .01)

    return .5*np.trapz(legendrePolynomial(order, x)*f(2**(-2)*x), dx=0.01)


# Numerical approximation to the scaling coeffisients
def approximatedScalingCoef(order, scale, translation, f):
    x = np.arange(0, 1, .0001)
    return 2**(-.5*scale) * \
        np.trapz(
                legendrePolynomial(order, x)
                * f(2**(-scale)*(x + translation)), dx=0.0001)


# Returns the scaling coeffisients
def scalingCoef(order, nr_poly, scale, translation, f):

    tmp = 0
    w = weights(nr_poly+1)
    x = roots(nr_poly+1)
    for q in range(0, w.size):
        tmp = tmp + w[q]*f(2**(-scale)*(x[q]+translation)) \
            * legendrePolynomial(order, float(x[q]))
    return 2**(-.5*scale)*tmp


def scalingCoefVec(nr_poly, scale, translation, f):
    tmp = np.empty(nr_poly)
    for i in range(nr_poly):
        tmp[i] = scalingCoef(i, nr_poly, scale, translation, f)
    return tmp


# Projects a function f onto a given set of polynomials and scale
def funcProj(scale, nr_poly, f, x):
    tmp = 0
    for j in range(0, nr_poly):
        for l in range(0, 2**scale):
            tmp = tmp+scaling_coef(j, nr_poly, scale, l, f) \
                * scaling(j, scale, l, x)
    return tmp


def integrate_scale(scale, nr_poly, f):
    tmp = 0
    x = np.arange(0, 1, 0.01)
    for j in range(0, nr_poly):
        for l in range(0, 2**scale):
            tmp = tmp+scalingCoef(j, nr_poly, scale, l, f) \
                * np.trapz(legendrePolynomial(j, x), dx=0.01)
    return tmp


def funcProjVec(scale, nr_poly, f, x):
    tmp = 0
    for j in range(2**scale):
        a = scalingCoefVec(nr_poly, scale, j, f)
        b = scalingVec(nr_poly, scale, j, x)
        tmp = tmp + (a*b).sum()
    return tmp
