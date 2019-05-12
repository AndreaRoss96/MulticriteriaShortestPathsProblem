import matplotlib.pyplot as plt

nodeList = []

def plotGraph(graph, resultsList, title, source, target) :
    
    xdata = []
    ydata = []
    vxdata = []
    vydata = []
    pxdata = []
    pydata = []

    for node in graph :
        if not(len(node.labelList) == 0) :
            vxdata.append(node.latitude)
            vydata.append(node.longitude)
        else :
            xdata.append(node.latitude)
            ydata.append(node.longitude)

    totpxData = []
    totpyData = []
    for nodeList in resultsList :
        for node in nodeList :
            pxdata.append(node.latitude)
            pydata.append(node.longitude)
        totpxData.append(pxdata)
        totpyData.append(pydata)
    
    plt.plot(vydata, vxdata, 'y.', markersize=1)
    plt.plot(ydata, xdata, '.', markersize=1)

    dim = len(totpxData) -1
  
    plt.plot(totpyData[0], totpxData[0], 'k-', markersize=1)
    miny, minx = list(totpyData[0]), list(totpxData[0])
    plt.plot(miny, minx, "r-")

    # plt.plot(totpyData[dim], totpxData[dim], 'rs', markersize=1)

    plt.plot(source.longitude, source.latitude, 'go')
    plt.plot(target.longitude, target.latitude, 'ro')
    plt.title(title)

    plt.show()
