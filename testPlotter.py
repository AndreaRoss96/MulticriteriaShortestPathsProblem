#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds

arches = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)
nodes = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)

# print(nodes[0].values.tolist())
print(nodes[1][0])
print(nodes[2][0])
plt.plot(nodes[1], nodes[2], '.', markersize=1)

# plt.plot(arches[0], '-')
plt.show()
# import matplotlib.pyplot as plt
# import time
# import random
 
# ysample = random.sample(range(-50, 50), 100)
 
# xdata = []
# ydata = []
 
# plt.show()
 
# axes = plt.gca()
# axes.set_xlim(0, 100)
# axes.set_ylim(-50, +50)
# line, = axes.plot(xdata, ydata, 'r-')
 
# for i in range(100):
#     xdata.append(i)
#     ydata.append(ysample[i])
#     line.set_xdata(xdata)
#     line.set_ydata(ydata)
#     plt.draw()
#     plt.pause(1e-17)
#     time.sleep(0.1)
 
# # add this if you don't want the window to disappear at the end
# plt.show()