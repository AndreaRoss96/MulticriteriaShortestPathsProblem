import sys
import time
import random

import pandas as pds
sys.path.append("algorithms/") # Has to be here to import the module in algorithms/
from algorithms.bicriteriaDijkstra import (binarySearchDijkBiCr,
                                           dijkstraBiCrit,
                                           dijkstraBiCrIteration)
from algorithms.lowerBoundImprovement import lowerBoundImprovementReversed                                           
from algorithms.labelSettingAlgorithm import labelSettingAlgorithm, lowerBoundImprovement
from Node import Node
from setup import graphBuilder
from utilities import initSingleNode
from graphPlotter import *

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)


graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

source = graph[1000]#23755]#2000]#
target = graph[1510]#27268]#2689]# #5142 or 2886

# counter = 0
# while counter < 10 :
#     initSingleNode(graph, source)
#     s, t = random.randint(1, 6232), random.randint(1, 6232)
#     if s == t :
#         continue
#     source = graph[s]#23755]#2000]#
#     target = graph[t]
#     labelSettingAlgorithm(source, target)
#     if len(target.labelList) > 1 :
#         counter += 1
#         print("source:", s, " target:", t)

# print("source:", s, " target:", t)

# print("s:", source.index, "-> t:", target.index)

# initSingleNode(graph, source)
# dijkstraBiCrit(source, target, 1)

# print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
# initSingleNode(graph, source)

# tmp_list= []
# precision = 0.2
# for n in range (0, 1):
#     initSingleNode(graph, source)
#     start = time.time()
#     infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
#     end = time.time()
#     tmp_list.append(end-start)
# print("AVGtime:", sum(tmp_list) / len(tmp_list))

#################
#### RESULTS ####
#################
# print("Using a precision of {2}: From {0.index} to {1.index} the solutions are:".format(source, target, precision))
# toPrint = []
# toGraph = []
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> peso_1:", distDang[0], " peso_2: ", distDang[1])
#     stringa = "({0}, {1}),".format(distDang[0], distDang[1])
#     toPrint.append(stringa)
#     toGraph.append((distDang[0], distDang[1]))

#     tmp_list= []


    
# precision = 0.05
# for n in range (0, 1):
#     initSingleNode(graph, source)
#     start = time.time()
#     infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
#     end = time.time()
#     tmp_list.append(end-start)
# print("AVGtime:", sum(tmp_list) / len(tmp_list))

#################
#### RESULTS ####
#################
# print("Using a precision of {2}: From {0.index} to {1.index} the solutions are:".format(source, target, precision))
# toPrint = []
# toGraph = []
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> peso_1:", distDang[0], " peso_2: ", distDang[1])
#     stringa = "({0}, {1}),".format(distDang[0], distDang[1])
#     toPrint.append(stringa)
#     toGraph.append((distDang[0], distDang[1]))

##########################################################################################
##########################################################################################
# print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
# initSingleNode(graph, source)

# tmp_list= []
# for n in range (0, 1):
#     initSingleNode(graph, source)
#     start = time.time()
#     infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
#     end = time.time()
#     tmp_list.append(end-start)
# print("AVGtime:", sum(tmp_list) / len(tmp_list))

#print(target.labelList)
#####################
#####  RESULTS  #####
#####################
# print("From {0.index} to {1.index} the solutions are:".format(source, target))
# toPrint = []
# toGraph = []
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> peso_1:", distDang[0], " peso_2: ", distDang[1])
#     stringa = "({0}, {1}),".format(distDang[0], distDang[1])
#     toPrint.append(stringa)
#     toGraph.append((distDang[0], distDang[1]))
# print("time:", end - start) # Print time
# print(*toPrint) # Print all the final results

# from graphPlotter import paretoGraph
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
# print(*dbgList, sep="->") # Print all the path in the form of node->node

##########################################################################################
##########################################################################################
print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    count = labelSettingAlgorithm(source, target) # algorithm
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))
print("len:", len(target.labelList))
print("loops:", count)
# for label in target.labelList :
#     print((label[0], label[1]))


#####################
#####  RESULTS  #####
#####################
# toPrint = []
# toParetoGrap = []
# for label in target.labelList :
#     print("distance:", label[0], "danger:", label[1], "predecessor:", label[3].index)
#     stringa = "({0}, {1}),".format(label[0], label[1])
#     toPrint.append(stringa)
#     toParetoGrap.append((label[0], label[1]))
# print("time:", end - start)  # Print time
# print(*toPrint)              # Print all the final results
# print(len(target.labelList)) # Length of the labelList 

#####################
### PARETO GRAPH #### Need the variable toGraph made in binary search algorithm
#####################
# from graphPlotter import doubleParetoGraph
# doubleParetoGraph(toGraph, toParetoGrap)

########################
##### BACKTRACKING #####
########################

# lista = [#(24844, 20539),
# # (37461, 26131),
# # (11802, 27410),
# # (1298, 23289),
# (37029, 32144),
# (28953, 25778),
# (18826, 37718),
# (31381, 32126),
# (1681, 31184),
# (2202, 25952)]
# from graphPlotter import bicriteriaPlotGraph
# for elem in lista:
#     s, t = elem[0], elem[1]
#     print("source:", s, "target:", t)
#     source = graph[s]
#     target = graph[t]
#     initSingleNode(graph, source)
#     labelSettingAlgorithm(source, target) # algorithm

graphList = []
for label in target.labelList :
    printList = []
    nodeList = [label[2]]
    while label[3] != None :
        node = label[3]
        nodeList.append(node)
        lenList = len(node.labelList)
        index = label[5] if label[5] < lenList else lenList - 1
        label = node.labelList[index]
        printList.append(node.index)
    graphList.append(nodeList)
    # print(*printList, sep="<-")
print(len(target.labelList))
    
bicriteriaPlotGraph(graph, graphList, "Bicriteria", source, target)


###################
### MAP'S GRAPH ###
###################
# from graphPlotter import bicriteriaPlotGraph
# bicriteriaPlotGraph(graph, graphList, "Bicriteria", source, target)

#########################################################################################
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
    count = lowerBoundImprovement(graph, source, target) # algorithm
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))
print("loops:", count)
# for label in target.labelList :
#     print((label[0], label[1]))

#####################
#####  RESULTS  #####
#####################
# print("all paths to target", target.index, ":")
# for label in target.labelList :
#     print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
# print("time:", end-start)
# print(len(target.labelList))

########################
##### BACKTRACKING #####
########################
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

###################
### MAP'S GRAPH ###
###################
# from graphPlotter import bicriteriaPlotGraph
# bicriteriaPlotGraph(graph, graphList,labelList


print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND refversed", "*"*25)

tmp_list= []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    lowerBoundImprovementReversed(source, target) # algorithm
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))
# for label in target.labelList :
#     print((label[0], label[1]))