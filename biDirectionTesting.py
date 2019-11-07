import sys
import time

import pandas as pds
sys.path.append("algorithms/") # Has to be here to import the module in algorithms/
from algorithms.bidirectional.bidirectionalBicriteria import bidirectionalBicriteriaAlgorithm
from Node import Node
from setup import graphBuilder
from utilities import initSingleNode

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

source = graph[2000]
target = graph[2689] #5142 or 2886


print("\n", "*"*40, "bidirection ALGORITHM", "*"*40)
initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1):
    initSingleNode(graph, source)
    start = time.time()
    bidirectionalBicriteriaAlgorithm(source, target) # algorithm
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))