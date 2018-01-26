def getfilter(type="H",flag=0,order_imp=4):
    import struct
    import numpy as np
    order = order_imp - 1
    name = "mwfilters/L_" + type + "0_" + str(order)
    filterFile = open(name, 'rb')
    filterData = filterFile.read()
    filterList = []
    for i in range((order_imp)*(order_imp)):
        rstart = i * 8
        rend = (i + 1) * 8
        filterList.append(struct.unpack_from("d",filterData[rstart:rend]))
    filterArray = np.array(filterList)
    filterMatrix = np.ndarray((order_imp, order_imp),buffer=filterArray)
    if (flag == 1):
        if (type == "G" and order_imp%2 != 0 ):
            sign_np = -1
        else:
            sign_np = 1
        for i in range(order_imp):
            for j in range(order_imp):
                sign_ij = 1
                if (((i+j)%2) == 0):
                    sign_ij = -1
                sign = sign_ij * sign_np
                filterMatrix[i,j] *= sign
    return filterMatrix
