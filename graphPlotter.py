import matplotlib.pyplot as plt

nodeList = []

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

    plt.show()

