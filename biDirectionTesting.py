import sys
import time

import pandas as pds
sys.path.append("algorithms/") # Has to be here to import the module in algorithms/
from algorithms.bidirectional.bidirectionalBicriteria import bidirectionalBicriteriaAlgorithm
from Node import Node
from setup import graphBuilder
from utilities import initSingleNode

dataN = pds.read_csv('graphs/5thousand2Nodes.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/5thousand2Arches.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

source = graph[2000]#23755]#2000]#
target = graph[2010]#27268]#2689]# #5142 or 2886


print("\n", "*"*40, "bidirection ALGORITHM", "*"*40)
initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1): # increase the second value to make an average
    initSingleNode(graph, source)
    start = time.time()
    paretoList = bidirectionalBicriteriaAlgorithm(source, target) # algorithm
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))
print(len(paretoList))

########################
##### BACKTRACKING #####
########################

# for elem in paretoList :
#     print(elem[0], elem[1])

# for paretoLabel in paretoList.values() :
#     print("ParetoLabel:", paretoLabel)
#     print(paretoLabel[2].directedLabelList[True])
#     for fwLabel in paretoLabel[2].directedLabelList[True] :
#         printListFw = []
#         while fwLabel[3] != None :
#             node = fwLabel[3]
            
#             lenList = len(node.labelList)
#             index = fwLabel[5] if fwLabel[5] < lenList else lenList - 1
#             fwLabel = node.directedLabelList[True][index]
#             printListFw.append(node.index)

#             for bwLabel in target.labelList :
#                 printListBw = []
#                 while bwLabel[3] != paretoLabel[2] : # as long the predecessor is != from the owner of the pareto label
#                     node = bwLabel[3]
                    
#                     lenList = len(node.labelList)
#                     index = bwLabel[5] if bwLabel[5] < lenList else lenList - 1
#                     bwLabel = node.directedLabelList[False][index]
#                     printListBw.append(node.index)
#                 print(*printListFw, *printListBw, sep="<-") 



