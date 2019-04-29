import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import numpy as np

nodeList = []

def plotGraph(graph, nodes, title) :
    
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
    plt.title(title)

    plt.show()

