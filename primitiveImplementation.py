#This module contains approximations and brute force appoaches
#which can be used to test more sophisticated implementations

# x is used for position

#Wavelet function at scale zero
def waveletScaleZero(order,nr_ploy,x):
    from getfilter import getfilter
    from scaling import scaling
    Sum = 0
    G0 = getfilter("G", 0, nr_ploy)
    G1 = getfilter("G", 1, nr_ploy)
   # print(G0)
   # print(G1)
    for i in range(nr_ploy):
        #print("G0[", order ,",",i,"]" ,"=" ,G0[order,i])
        #print("scaling(",i,",",1,",",0,",",x,")","=",sc.scaling(i, 1, 0, x) )
        #print("restult",G0[order, i]*sc.scaling(i, 1, 0, x)/np.sqrt(2) )
        #Check if this should be a pluss or minus
        wavelet = (G0[order, i]*scaling(i, 1, 0, x)) + \
        (G1[order, i]*scaling(i, 1, 1, x))
        Sum += wavelet
    return Sum

#Scaled wavelet function
def waveletScaled(order, scale, translation, nr_poly, x):
        return 2**(scale/2)*waveletScaleZero(order,nr_poly,(2**scale)*x-translation)

def approximatedScalingCoef(order,scale,translation,f):
    from scaling import legendre_polynomial
    from numpy import arange, trapz
    x = arange(0,1,.01)
    return 2**(-.5*scale)*trapz(legendre_polynomial(order,x)*f(2**(-scale)*(x + translation)),dx=0.01)

def normWavletScaleZero(order_wavelet_one, order_wavelet_two):
    from numpy import arange, trapz
    dx = 0.001
    x = arange(0.,1.,dx)

    return trapz(waveletScaleZero(order_wavelet_one,4,x)*waveletScaleZero(order_wavelet_two,4,x),dx=dx)

def normWavletScale(order_wavelet_one,scale_wavelet_one, order_wavelet_two, scale_wavelet_two,translation_one,translation_two):
    from numpy import arange, trapz
    dx = 0.001
    x = arange(0.,1.,dx)

    return trapz(waveletScaled(order_wavelet_one,scale_wavelet_one,translation_one,4,x) \
        *waveletScaled(order_wavelet_two,scale_wavelet_two,translation_two,4,x),dx=dx)




if __name__ == '__main__':
    def testFunc(x):
        from numpy import sin, pi
        return sin(2.0*pi*x)
