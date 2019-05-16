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
source = graph[6429]
target = graph[6531] #5142 or 2886

initSingleNode(graph, source)
print("alpha = 1 shortest")
dijkstraBiCrit(source, target, 1)
dbgList = []
pointer = target
while pointer != source :
    dbgList.append(pointer.index)
    pointer = pointer.predecessor
dbgList.append(pointer.index)
dbgList = reversed(dbgList)
print(*dbgList, sep="->")

# print("*"*40, "BICRITERIA DIJKSTRA", "*"*40)
# start = time.time()
# infoList = dijkstraBiCrIteration(graph, source, target, 0.02)
# end = time.time()

# print("From {0.index} to {1.index} the solutions are:".format(source, target))
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> distance:", distDang[0], "and danger: ", distDang[1])
# print("time:", end - start)

# #########################################################################################

print("\n", "*"*30, "BICRITERIA DIJKSTRA WITH BINARY SEARCH", "*"*30)
initSingleNode(graph, source)
start = time.time()
infoList = binarySearchDijkBiCr(graph, source, target)
end = time.time()
print("From {0.index} to {1.index} the solutions are:".format(source, target))
# for distDang, alpha in infoList.items() :
#     print("With α =", alpha, "=> distance:", distDang[0], "and danger: ", distDang[1])
print("time:", end - start)

#  #########################################################################################


print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
initSingleNode(graph, source)

start = time.time()
labelSettingAlgorithm(source, target)
end = time.time()

toPrint = []

print("all paths to target", target.index, ":")
# for label in target.labelList :
#     print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
#     stre = "(" + str(label[0]) + ', ' + str(label[1]) + ")"
#     toPrint.append(stre)
print("time:", end-start)
print(len(target.labelList))
# print(str(toPrint))

########################
# # ### BACKTRACKING V
# label = target.labelList[0]
# nodeList = [label[2].index]
graphList = []
# print(target.labelList)
# for label in target.labelList :
# label = target.labelList[len(target.labelList) - 1]
# printList = []
# nodeList = [label[2]]
# # print(label[0])
# summa = label[0]
# sumList = []
# while label[3] is not None :
#     node = label[3]        # get predecessor
#     nodeList.append(node)
#     index = label[5] # if label[5] < lenList else lenList - 1
#     # print(index)
#     if label[2] != target :
#         sumList.append(summa - label[0])
#         summa = label[0]
#     label = node.labelList[index] # get the label originator
#     # print(label)
#     printList.append(node.index)

# Sum = sum(sumList)
# # print("Value:", Sum)
# nodeList.append(target)
# graphList.append(nodeList)
# printList = reversed(printList)
# print(*printList, sep=", ")

# from biCriteriaGraphPlotter import plotGraph
# plotGraph(graph, graphList, "Bicriteria", source, target)

 #########################################################################################

print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)

initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1):
    start = time.time()
    lowerBoundImprovement(graph, source, target)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

# print("all paths to target", target.index, ":")
# for label in target.labelList :
#     print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
print("time:", end-start)
print(len(target.labelList))
