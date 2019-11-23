import sys
import time

import pandas as pds
sys.path.append("algorithms/") # Has to be here to import the module in algorithms/
from algorithms.bicriteriaDijkstra import (binarySearchDijkBiCr,
                                           dijkstraBiCrit,
                                           dijkstraBiCrIteration)
from algorithms.labelSettingAlgorithm import labelSettingAlgorithm, lowerBoundImprovement
from algorithms.lowerBoundImprovement import lowerBoundImprovementReversed
from Node import Node
from setup import graphBuilder
from utilities import initSingleNode
from algorithms.bidirectional.bidirectionalBicriteria import bidirectionalBicriteriaAlgorithm


dataN = pds.read_csv('graphs/5thousand2Nodes.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/5thousand2Arches.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

source = graph[0]#23755]#2000]#
target = graph[1]

print("-" * 40, "1", "-"*40)

# print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
# initSingleNode(graph, source)
# precision = 0.05
# start = time.time()
# infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

# print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
# initSingleNode(graph, source)
# start = time.time()
# infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

# print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
# for v in visitedNodes:
#     v.resetValue(True) 
# dijkstraBiCrit(source, target, 1)
# end = time.time()
# print("AVGtime:", end-start)

# print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovement(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)

# print("\n", "*"*40, "lower bound reversed", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovementReversed(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)


# print("\n", "*"*40, "bidirection", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# pareto = bidirectionalBicriteriaAlgorithm(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(pareto[0]))
# print("loops:", pareto[1])

###############################################################################################################################

target = graph[10]

print("-" * 40, "10", "-"*40)

# print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
# initSingleNode(graph, source)
# precision = 0.05
# start = time.time()
# infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

# print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
# initSingleNode(graph, source)
# start = time.time()
# infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

# print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
# for v in visitedNodes:
#     v.resetValue(True) 
# dijkstraBiCrit(source, target, 1)
# end = time.time()
# print("AVGtime:", end-start)


# print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovement(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)


# print("\n", "*"*40, "lower bound reversed", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovementReversed(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)



# print("\n", "*"*40, "bidirection", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# pareto = bidirectionalBicriteriaAlgorithm(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(pareto[0]))
# print("loops:", pareto[1])

###############################################################################################################################

target = graph[100]

print("-" * 40, "100", "-"*40)

# print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
# initSingleNode(graph, source)
# precision = 0.05
# start = time.time()
# infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

# print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
# initSingleNode(graph, source)
# start = time.time()
# infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
initSingleNode(graph, graph[2000])
start = time.time()
count = labelSettingAlgorithm(graph[2000], graph[2010]) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(target.labelList))
print("loops:", count)
# for label in target.labelList :
#     print((label[0], label[1]))


for label in graph[2010].labelList :
    printList = []
    nodeList = [label[2]]
    while label[3] != None :
        node = label[3]
        nodeList.append(node)
        lenList = len(node.labelList)
        index = label[5] if label[5] < lenList else lenList - 1
        label = node.labelList[index]
        printList.append(node.index)
    print(*printList, sep="<-")

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
# for v in visitedNodes:
#     v.resetValue(True) 
# dijkstraBiCrit(source, target, 1)
# end = time.time()
# print("AVGtime:", end-start)

# print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovement(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)


# print("\n", "*"*40, "lower bound reversed", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovementReversed(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)


print("\n", "*"*40, "bidirection", "*"*40)
initSingleNode(graph, source)
start = time.time()
pareto = bidirectionalBicriteriaAlgorithm(source, target)
end = time.time()
print("AVGtime:", end-start)
print(len(pareto[0]))
print("loops:", pareto[1])
# for label in pareto[0] :
#     print((label[0], label[1]))

###############################################################################################################################

target = graph[300]

print("-" * 40, "300", "-"*40)

# print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
# initSingleNode(graph, source)
# precision = 0.05
# start = time.time()
# infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

# print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
# initSingleNode(graph, source)
# start = time.time()
# infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

# print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
# for v in visitedNodes:
#     v.resetValue(True) 
# dijkstraBiCrit(source, target, 1)
# end = time.time()
# print("AVGtime:", end-start)

# print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovement(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)


# print("\n", "*"*40, "lower bound reversed", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovementReversed(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)



# print("\n", "*"*40, "bidirection", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# pareto = bidirectionalBicriteriaAlgorithm(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(pareto[0]))
# print("loops:", pareto[1])

###############################################################################################################################

target = graph[400]

print("-" * 40, "400", "-"*40)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)
precision = 0.05
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
initSingleNode(graph, source)
start = time.time()
infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

# print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
# for v in visitedNodes:
#     v.resetValue(True) 
# dijkstraBiCrit(source, target, 1)
# end = time.time()
# print("AVGtime:", end-start)

# print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovement(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)


# print("\n", "*"*40, "lower bound reversed", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = lowerBoundImprovementReversed(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)


# print("\n", "*"*40, "bidirection", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# pareto = bidirectionalBicriteriaAlgorithm(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(pareto[0]))
# print("loops:", pareto[1])

###############################################################################################################################

target = graph[700]

print("-" * 40, "700", "-"*40)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)
precision = 0.05
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
initSingleNode(graph, source)
start = time.time()
infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

# print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
# for v in visitedNodes:
#     v.resetValue(True) 
# dijkstraBiCrit(source, target, 1)
# end = time.time()
# print("AVGtime:", end-start)

# print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
# initSingleNode(graph, source)
# start = time.time()
# lowerBoundImprovement(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*40, "lower bound reversed", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# lowerBoundImprovementReversed(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*40, "bidirection", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# pareto = bidirectionalBicriteriaAlgorithm(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(pareto[0]))
# print("loops:", pareto[1])

###############################################################################################à

target = graph[5000]

print("-" * 40, "5000", "-"*40)

# print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
# initSingleNode(graph, source)
# precision = 0.05
# start = time.time()
# infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(infoList))

print("\n", "*"*35, "DIJKSTRA BICRITERIA BINARY SEARCH", "*"*35)
initSingleNode(graph, source)
start = time.time()
infoList = binarySearchDijkBiCr(graph, source, target) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

# print("\n", "*"*40, "LABEL SETTING ALGORITHM", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# count = labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))
# print("loops:", count)

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
# for v in visitedNodes:
#     v.resetValue(True) 
# dijkstraBiCrit(source, target, 1)
# end = time.time()
# print("AVGtime:", end-start)

# print("\n", "*"*25, "LABEL SETTING ALGORITHM LOWER BOUND IMPROVEMENT", "*"*25)
# initSingleNode(graph, source)
# start = time.time()
# lowerBoundImprovement(graph, source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*40, "lower bound reversed", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# lowerBoundImprovementReversed(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*40, "bidirection", "*"*40)
# initSingleNode(graph, source)
# start = time.time()
# pareto = bidirectionalBicriteriaAlgorithm(source, target)
# end = time.time()
# print("AVGtime:", end-start)
# print(len(pareto[0]))
# print("loops:", pareto[1])