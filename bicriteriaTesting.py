from Node import Node
from setup import graphBuilder
import time
import pandas as pds

print(pds.__file__)

from utilities import initSingleNode
from labelSettingAlgorithm import labelSettingAlgorithm
from labelSettingAlgorithm import lowerBoundImprovement
from bicriteriaDijkstra import dijkstraBiCrit
from bicriteriaDijkstra import binarySearchDijkBiCr
from bicriteriaDijkstra import dijkstraBiCrIteration

dataN = pds.read_csv('graphs/berlin_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/berlin_arcs.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

source = graph[6660]
target = graph[33083] #5142 or 2886

# print("s:", source.index, "-> t:", target.index)

initSingleNode(graph, source)
dijkstraBiCrit(source, target, 1)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)

tmp_list= []
precision = 0.05
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    infoList = dijkstraBiCrIteration(graph, source, target, precision)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))
print("Using a precision of {2}: From {0.index} to {1.index} the solutions are:".format(source, target, precision))
# toPrint = []
# toGraph = []
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> distance:", distDang[0], "and danger: ", distDang[1])
    # stringa = "({0}, {1}),".format(distDang[0], distDang[1])
    # toPrint.append(stringa)
    # toGraph.append((distDang[0], distDang[1]))

# #########################################################################################
print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    infoList = binarySearchDijkBiCr(graph, source, target)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

#####################
#####  RESULTS  #####
#####################
print("From {0.index} to {1.index} the solutions are:".format(source, target))
# toPrint = []
# toGraph = []
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> distance:", distDang[0], "and danger: ", distDang[1])
    # stringa = "({0}, {1}),".format(distDang[0], distDang[1])
    # toPrint.append(stringa)
    # toGraph.append((distDang[0], distDang[1]))
print("time:", end - start)
# print(*toPrint)
from graphPlotter import paretoGraph
# paretoGraph(toGraph)


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
toPrint = []
toParetoGrap = []
# for label in target.labelList :
#     # print("distance:", label[0], "danger:", label[1], "predecessor:", label[3].index)
#     stringa = "({0}, {1}),".format(label[0], label[1])
#     toPrint.append(stringa)
#     toParetoGrap.append((label[0], label[1]))
print("time:", end - start)
# print(*toPrint)
print(len(target.labelList))

from graphPlotter import doubleParetoGraph
# doubleParetoGraph(toGraph, toParetoGrap)
# toPrint = []
# print("From {0.index} to {1.index} the solutions are:".format(source, target))
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

# from graphPlotter import bicriteriaPlotGraph
# bicriteriaPlotGraph(graph, graphList, "Bicriteria", source, target)

 #########################################################################################

print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
tmp_list = []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()

    dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
    initSingleNode(graph, source)
    dijkstraBiCrit(source, target, 1) # shortest path => "


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
print("all paths to target", target.index, ":")
# for label in target.labelList :
#     print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
print("time:", end-start)
print(len(target.labelList))
