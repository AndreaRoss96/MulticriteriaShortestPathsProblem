# #from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pds

# arches = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)
# nodes = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)

# print(nodes[0].values.tolist())

# # plt.plot(nodes[1], nodes[2], '.', markersize=0.5)
# plt.plot(arches[0], '-')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

plt.ion()
for i in range(50):
    y = np.random.random([10,1])
    plt.plot(y)
    plt.draw()
    plt.pause(0.5)
    plt.clf()