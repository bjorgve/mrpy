def getfilter(type="H", flag=0, order_imp=4):
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
        filterList.append(struct.unpack_from("d", filterData[rstart:rend]))
    filterArray = np.array(filterList)
    filterMatrix = np.ndarray((order_imp, order_imp), buffer=filterArray)
    if (flag == 1):
        if type == "G":
            for i in range(order_imp):
                for j in range(order_imp):
                    filterMatrix[i, j] = \
                        (-1)**(i+j+order_imp)*filterMatrix[i, j]
        if type == "H":
            for i in range(order_imp):
                for j in range(order_imp):
                    filterMatrix[i, j] = (-1)**(i+j+1)*filterMatrix[i, j]
                    # According to Adaptive solutions by Alptert this should
                    # be (-1)**(i+j). But according to experiments the current
                    # implementation is correct.
        else:
            print("Error: not valid type")
    return filterMatrix
