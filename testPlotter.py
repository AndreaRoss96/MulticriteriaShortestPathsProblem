#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds

arches = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)
nodes = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)

print(nodes[0].values.tolist())

# plt.plot(data[1], data[2], ',')
# plt.show()
