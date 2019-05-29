import matplotlib.pyplot as plt

def plotGraph(graph, nodes, title, source, target) :
    
    xdata = []
    ydata = []
    vxdata = []
    vydata = []
    pxdata = []
    pydata = []

    for node in graph :
        if node.visited :
            vxdata.append(node.latitude)
            vydata.append(node.longitude)
        else :
            xdata.append(node.latitude)
            ydata.append(node.longitude)
    
    for node in nodes :
        pxdata.append(node.latitude)
        pydata.append(node.longitude)
    
    plt.plot(vydata, vxdata, 'y.', markersize=1)
    plt.plot(ydata, xdata, '.', markersize=1)
    plt.plot(pydata, pxdata, 'r-', markersize=1)

    plt.plot(source.longitude, source.latitude, 'go')
    plt.plot(target.longitude, target.latitude, 'ro')

    plt.title(title)
    plt.xlabel('Latitude', fontsize=15)
    plt.ylabel('Longitude', fontsize=15)

    plt.show()

def bicriteriaPlotGraph(graph, resultsList, title, source, target) :
    
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

    plt.plot(totpyData[0], totpxData[0], 'r-', markersize=1)
    
    plt.plot(source.longitude, source.latitude, 'go')
    plt.plot(target.longitude, target.latitude, 'ro')
    plt.title(title)
    plt.xlabel('Latitude', fontsize=15)
    plt.ylabel('Longitude', fontsize=15)

    plt.show()

def paretoGraph(result) :

    distList = []
    dangList = []

    for dist, dang in result :
        distList.append(dist)
        dangList.append(dang)
    
    plt.plot(distList, dangList, 'rs', markersize=5)
    plt.xlabel('Distance', fontsize=18)
    plt.ylabel('Danger', fontsize=18)
    plt.show()

def doubleParetoGraph(resultA, resultB) :

    distListA = []
    dangListA = []

    distListB = []
    dangListB = []

    for dist, dang in resultA :
        distListA.append(dist)
        dangListA.append(dang)

    for dist, dang in resultB :
        distListB.append(dist)
        dangListB.append(dang)
    
    plt.plot(distListA, dangListA, 'rs', markersize=5)
    plt.plot(distListB, dangListB, 'yo', markersize=3)
    plt.xlabel('Distance', fontsize=18)
    plt.ylabel('Danger', fontsize=18)
    plt.show()