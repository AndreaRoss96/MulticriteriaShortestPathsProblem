import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

nodeList = []

def plotGraph(graph, nodes) :

    nodeList.extend(nodes)
    fig = plt.figure()

    xdata = []
    ydata = []

    for point in graph :
        xdata.append(point.x)
        ydata.append(point.y)
    
    # plt.clear()
    plt.plot(xdata, ydata, ',')

    ani = animation.FuncAnimation(fig, animate, interval = 1)
    plt.show()

def animate(i) :
    if counter < len(nodeList) :
        counter = counter + 1
        plt.plot(nodeList[counter].x, nodeList[counter].y, 'ro')


