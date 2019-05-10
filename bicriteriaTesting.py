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
source = graph[22066]
target = graph[9174]


print("*"*40, "BICRITERIA DIJKSTRA", "*"*40)
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, 0.02)
end = time.time()

print("From {0.index} to {1.index} the solutions are:".format(source, target))
for distDang, alpha in infoList.items() :
    print("With α =", alpha, "=> distance :", distDang[0], "and danger: ", distDang[1])
print("time:", end - start)

#########################################################################################

print("\n", "*"*30, "BICRITERIA DIJKSTRA WITH BINARY SEARCH", "*"*30)
initSingleNode(graph, source)
start = time.time()
infoList = binarySearchDijkBiCr(graph, source, target)
end = time.time()
print("From {0.index} to {1.index} the solutions are:".format(source, target))
for distDang, alpha in infoList.items() :
    print("With α =", alpha, "=> distance :", distDang[0], "and danger: ", distDang[1])
print("time:", end - start)

#########################################################################################

print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
initSingleNode(graph, source)

start = time.time()
labelSettingAlgorithm(source, target)
end = time.time()

print("all paths to target", target.index, ":")
for label in target.labelList :
    print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
print("time:", end-start)

# label = target.labelList[0]
#########################
# BACKTRACKING V
# while label[3] != None :
#     index = label[4]
#     node = label[3]
#     label = node.labelList[index]
#     print(label[2].index)

print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
initSingleNode(graph, source)

start = time.time()
lowerBoundImprovement(graph, source, target)
end = time.time()

print("all paths to target", target.index, ":")
for label in target.labelList :
    print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")
print("time:", end-start)
