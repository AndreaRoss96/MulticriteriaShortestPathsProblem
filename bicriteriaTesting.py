from node import Node
from setup import graphBuilder
import time
import pandas as pds

from utilities import initSingleNode
from labelSettingAlgorithm import labelSettingAlgorithm

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)


graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())
source = graph[2000]
target = graph[2229]

print("*"*40, "LABEL SETTING ALGORITHM", "*"*40)
initSingleNode(graph, source)

start = time.time()
labelSettingAlgorithm(source, target)
end = time.time()

print("time:", end-start)
print("all path to target", target.index, ":")
for label in target.labelList :
    print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")