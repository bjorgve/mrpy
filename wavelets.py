from getfilter import getfilter
import numpy as np
from scaling import scaling

def getScaleVec(nr_poly,scale,translation,x):
    tmp = np.empty(nr_poly)
    for order in range(tmp.size):
      #  print("scaling(",order,",",scale,",",0,",",x,")","=",sc.scaling(order, scale, translation, x) )
        tmp[order] = scaling(order,scale,translation,x)
    return tmp

def wavelet(nr_poly,x):
    G0 = getfilter("G",0,nr_poly)
    G1 = getfilter("G",1,nr_poly)
  #  print(G0)
    #Check if this should be a pluss or minus
    return np.dot(G0,getScaleVec(nr_poly,1,0,x))/np.sqrt(2.0)  + \
            np.dot(G1,getScaleVec(nr_poly,1,1,x))/np.sqrt(2.0)

def waveletScaled(scale,translation,nr_poly,x):
    G0 = getfilter("G",0,nr_poly)
    G1 = getfilter("G",1,nr_poly)
  #  print(G0)
    #Check if this should be a pluss or minus
    return np.dot(G0,getScaleVec(nr_poly,scale+1,translation*2,x))  + \
            np.dot(G1,getScaleVec(nr_poly,scale+1,translation*2+1,x))

if __name__ == '__main__':
    print(wavelet(1,.1))
