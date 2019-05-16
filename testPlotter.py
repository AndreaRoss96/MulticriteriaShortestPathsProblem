#from mpl_toolkits.basemap import Basemap
#TODO: DELETE THIS
import matplotlib.pyplot as plt
import numpy as np
import pandas as pds

arches = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)
nodes = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)

# lista = [2000, 2040, 1991, 29066, 28548, 28492, 27200, 2948, 7997, 4886, 16084, 28519, 28518, 28735, 28537, 351, 16139, 15408, 25604, 15397, 27113, 25812, 19731, 19744, 27891, 26128, 26104, 26041, 26096, 16725, 1112, 2886] # NOT LEGIT
# lista = [2000, 2040, 1991, 27892, 2683, 22019, 2948, 7997, 4886, 16084, 28518, 28735, 28537, 351, 16139, 15408, 27432, 25812, 19731, 19744, 27891, 26128, 26104, 26041, 26096, 16725, 1112, 2886] # LEGIT
# lista = [2000, 2040, 1991, 27892, 2683, 22019, 2948, 7997, 4886, 16084, 28518, 28735, 28537, 351, 16139, 15408, 25604, 15397, 27113, 25812, 19731, 19744, 27891, 26128, 26104, 26041, 26096, 28629, 28874, 1112]
# lista = [2000, 2040, 1991, 27892, 2683, 22019, 2948, 7997, 4886, 16084, 28518, 28735, 28537, 351, 16139, 15408, 25604, 15397, 27113, 25812, 19731, 19744, 27891, 26128, 26104, 26041, 26096, 28629, 28874, 1112, 2886] # OFFICIAL
# somma = []
# for i in range(1, len(lista)) :
#     a = lista[i-1]
#     b = lista[i]
#     print(a, "->", b)
#     var = arches.loc[(arches[0] == a) & (arches[1] == b)].values
#     if len(var) == 2 :
#         var = min(var[0][2], var[1][2])
#     elif len(var) > 2 :
#         print("maledetto dio")
#     else :
#         var = var[0][2]
#     somma.append(var)

# print(sum(somma))

# print(arches.loc[(arches[0] == 1112) & (arches[1] == 2886)].values[0][2])
print(arches.loc[arches[0] == 19524].values)

# save = arches.values.tolist()
# # print(save)
# tmp = 0
# # print(save[437])
# for id, elem in enumerate(save) :
#     if tmp == elem[1] :
#        print(arches.loc[arches[0] == save[id][0]].values)
#     else :
#         tmp = elem[1] 

# data = [(2010, 2), (2009, 4), (1989, 8), (2009, 7)]

# for k, val in data:
#     print("k:", k, "val:", val)
