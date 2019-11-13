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


dataN = pds.read_csv('graphs/200thousand2Nodes.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/200thousand2Arches.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

source = graph[0]#23755]#2000]#
target = graph[1]

print("-" * 40, "1", "-"*40)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)
precision = 0.05
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

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
# labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
# initSingleNode(graph, source)
# dijkstraBiCrit(source, target, 1) # shortest path => "
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

print("\n", "*"*40, "bidirection", "*"*40)
initSingleNode(graph, source)
start = time.time()
bidirectionalBicriteriaAlgorithm(source, target)
end = time.time()
print("AVGtime:", end-start)
print(len(target.labelList))

###############################################################################################################################

target = graph[10]

print("-" * 40, "10", "-"*40)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)
precision = 0.05
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

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
# labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
# initSingleNode(graph, source)
# dijkstraBiCrit(source, target, 1) # shortest path => "
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


print("\n", "*"*40, "bidirection", "*"*40)
initSingleNode(graph, source)
start = time.time()
bidirectionalBicriteriaAlgorithm(source, target)
end = time.time()
print("AVGtime:", end-start)
print(len(target.labelList))

###############################################################################################################################

target = graph[100]

print("-" * 40, "100", "-"*40)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)
precision = 0.05
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

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
# labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
# initSingleNode(graph, source)
# dijkstraBiCrit(source, target, 1) # shortest path => "
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


print("\n", "*"*40, "bidirection", "*"*40)
initSingleNode(graph, source)
start = time.time()
bidirectionalBicriteriaAlgorithm(source, target)
end = time.time()
print("AVGtime:", end-start)
print(len(target.labelList))

###############################################################################################################################

target = graph[300]

print("-" * 40, "300", "-"*40)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)
precision = 0.05
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

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
# labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
# initSingleNode(graph, source)
# dijkstraBiCrit(source, target, 1) # shortest path => "
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


print("\n", "*"*40, "bidirection", "*"*40)
initSingleNode(graph, source)
start = time.time()
bidirectionalBicriteriaAlgorithm(source, target)
end = time.time()
print("AVGtime:", end-start)
print(len(target.labelList))

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
# labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
# initSingleNode(graph, source)
# dijkstraBiCrit(source, target, 1) # shortest path => "
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

print("\n", "*"*40, "bidirection", "*"*40)
initSingleNode(graph, source)
start = time.time()
bidirectionalBicriteriaAlgorithm(source, target)
end = time.time()
print("AVGtime:", end-start)
print(len(target.labelList))

###############################################################################################################################

target = graph[500]

print("-" * 40, "500", "-"*40)

print("\n", "*"*35, "DIJKSTRA BICRITERIA ITERATION", "*"*35) #(10,25),(20,12),(5, 60)
initSingleNode(graph, source)
precision = 0.05
start = time.time()
infoList = dijkstraBiCrIteration(graph, source, target, precision) # algorithm
end = time.time()
print("AVGtime:", end-start)
print(len(infoList))

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
# labelSettingAlgorithm(source, target) # algorithm
# end = time.time()
# print("AVGtime:", end-start)
# print(len(target.labelList))

# print("\n", "*"*30, "DIJKSTRA PREPROCESSING", "*"*30)
# initSingleNode(graph, source)
# start = time.time()
# dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
# initSingleNode(graph, source)
# dijkstraBiCrit(source, target, 1) # shortest path => "
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

print("\n", "*"*40, "bidirection", "*"*40)
initSingleNode(graph, source)
start = time.time()
bidirectionalBicriteriaAlgorithm(source, target)
end = time.time()
print("AVGtime:", end-start)
print(len(target.labelList))