from node import Node
from setup import graphBuilder
import time
import pandas as pds

from utilities import initSingleNode
from labelSettingAlgorithm import labelSettingAlgorithm
from labelSettingAlgorithm import lowerBoundImprovement
from bicriteriaDijkstra import dijkstraBiCrit
from bicriteriaDijkstra import binarySearchDijkBiCr
from bicriteriaDijkstra import dijkstraBiCrIteration

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)


graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())
source = graph[15426]
target = graph[2070] #5142 or 2886

# print("s:", source.index, "-> t:", target.index)

initSingleNode(graph, source)
dijkstraBiCrit(source, target, 1)

# #########################################################################################
print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    binarySearchDijkBiCr(graph, source, target)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

#####################
#####  RESULTS  #####
#####################
# print("From {0.index} to {1.index} the solutions are:".format(source, target))
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> distance:", distDang[0], "and danger: ", distDang[1])
# print("time:", end - start)

######################
#### BACKTRACKING ####
######################
# dbgList = []
# pointer = target
# while pointer != source :
#     dbgList.append(pointer.index)
#     pointer = pointer.predecessor
# dbgList.append(pointer.index)
# dbgList = reversed(dbgList)
# print(*dbgList, sep="->")

#  #########################################################################################
print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    labelSettingAlgorithm(source, target)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

#####################
#####  RESULTS  #####
#####################
# toPrint = []
# print("all paths to target", target.index, ":")
# for label in target.labelList :
#     print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
#     stre = "(" + str(label[0]) + ', ' + str(label[1]) + ")"
#     toPrint.append(stre)
# print("time:", end-start)
# print(len(target.labelList)) # print length of label list
# print(str(toPrint))

########################
##### BACKTRACKING #####
# graphList = []
# for label in target.labelList :
#     printList = []
#     nodeList = [label[2]]
#     while label[3] != None :
#         node = label[3]
#         nodeList.append(node)
#         lenList = len(node.labelList)
#         index = label[5] if label[5] < lenList else lenList - 1
#         label = node.labelList[index]
#         printList.append(node.index)
#     graphList.append(nodeList)
    # print(*printList, sep="<-")

from biCriteriaGraphPlotter import plotGraph
plotGraph(graph, graphList, "Bicriteria", source, target)

 #########################################################################################

print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
tmp_list = []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()

    dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
    bestDanger = target.danger
    initSingleNode(graph, source)
    dijkstraBiCrit(source, target, 1) # shortest path => "
    bestDistance = target.distance


    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)

tmp_list= []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    lowerBoundImprovement(graph, source, target)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

#####################
#####  RESULTS  #####
#####################
# print("all paths to target", target.index, ":")
# for label in target.labelList :
#     print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
# print("time:", end-start)
# print(len(target.labelList))
