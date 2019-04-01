#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds

arches = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)
nodes = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)

# print(nodes[0].values.tolist())
# print(arches.loc[(arches[0] == 2000) & (arches[1] == 2040)])
# print(arches.loc[arches[0] == 26].values)

# save = arches.values.tolist()
# # print(save)
# tmp = 0
# # print(save[437])
# for id, elem in enumerate(save) :
#     if tmp == elem[1] :
#        print(arches.loc[arches[0] == save[id][0]].values)
#     else :
#         tmp = elem[1] 

data = [(2010, 2), (2009, 4), (1989, 8), (2009, 7)]

for k, val in data:
    print("k:", k, "val:", val)