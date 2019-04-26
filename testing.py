from node import Node
from setup import graphBuilder
import time
import random 
import pandas as pds

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)


graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())


#######################################
### MONO CRITERIA ALGORITHM TESTING ###
#######################################

from dijkstra import dijkstraOneToAll
from dijkstra import dijkstraOneToOne
from dijkstra import dijkstraListOfCandidate
from a_star import a_star
from graphPlotter import plotGraph
from utilities import initSingleNode

"""
for the right test start := 2000, target := 2689 the solution are like:
    weight: 5840
    2000->2040->1991->27892->2683->22019->2948->7997->4886->16084->28518->28735->28537->351->16139->15408->25604->15397->27113->25812->19731->19744->27891->26128->26104->26041->26096->28629->28874->1112->2886->19524->19560->19520->5142->13483->27078->29053->15119->27059->29039->28929->4636->18403->28348->1303->14605->18414->18505->4693->18413->18385->4694->18415->18400->18507->27047->27111->27107->27096->27068->27066->28919->27217->27191->27212->27240->27279->27278->27093->4508->9458->4738->27065->4646->4661->2689

random.randint(0, 2689)
"""
source = graph[2000]
target = graph[2689] # there's a problem with the 415th node

"""++++++++++++++++++++++++++++++++++++++++++++++++
************** ONE -> ALL ****************
"""
print("*"*40, "ONE TO ALL", "*"*40)
initSingleNode(graph, source)

start = time.time()
dijkstraOneToAll(graph, source)
end = time.time()

print("time:", end-start)
print("from", source.index, "to", target.index, "the weight of the path is:", source.shortestPaths.get(target))

dbgList = []
pointer = target
while pointer != source :
    dbgList.append(pointer.index)
    pointer = pointer.predecessor
dbgList.append(pointer.index)
dbgList = reversed(dbgList)

print(*dbgList, sep="->")





"""+++++++++++++++++++++++++++++++++++++++++++++++++
************** ONE -> ONE ****************
"""
print("*"*40, "ONE TO ONE", "*"*40)
initSingleNode(graph, source)

start = time.time()
#dijkstraOneToOne(graph, source, target)
end = time.time()

print("time:", end-start)





"""+++++++++++++++++++++++++++++++++++++++++++++++++
************** LIST OF CANDIDATE ****************
"""
print("*"*40, "LIST OF CANDIDATE", "*"*40)
initSingleNode(graph, source)

tmp_list= []

for n in range (0, 1):
    start = time.time()
    dijkstraListOfCandidate(graph, source, target)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

print("from",source.index, "to", target.index, "the weight of the path is:", target.minWeight)

dbgList = []
graphList = []
pointer = target
while pointer != source :
    dbgList.append(pointer.index)
    graphList.append(pointer)
    pointer = pointer.predecessor
dbgList.append(pointer.index)
dbgList = reversed(dbgList)
print(*dbgList, sep="->")

from provaTkinter import createGraph
# createGraph(graph, reversed(graphList))

plotGraph(graph, reversed(graphList))







"""+++++++++++++++++++++++++++++++++++++++++++++++++
************** A STAR ****************
"""
print("*"*40, "A STAR", "*"*40)
initSingleNode(graph, source)

tmp_list = []

for n in range (0, 1):
    start = time.time()
    a_star(graph, source, target)
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

print("from",source.index, "to", target.index, "the weight of the path is:", target.minWeight)

dbgList = []
graphList = []
pointer = target
while pointer != source :
    dbgList.append(pointer.index)
    graphList.append(pointer)
    pointer = pointer.predecessor
dbgList.append(pointer.index)
dbgList = reversed(dbgList)

print(*dbgList, sep="->")

plotGraph(graph, reversed(graphList))


#######################################
### BICRITERIA ALGORITHM TESTING    ###
#######################################
from bicriteriaDijkstra import dijkstraBiCrit



print("*"*40, "BICRITERIA DIJKSTRA", "*"*40)
alpha = 0

tmp_list= []

while alpha <= 1 :
    initSingleNode(graph, source)
    start = time.time()
    dijkstraBiCrit(graph, source, target, alpha)
    end = time.time()
    tmp_list.append(end-start)
    print("from {0.index} to {1.index} the distance is {1.distance} and the danger is {1.danger} -- \u03B1 = {2}".format(source, target, alpha))
    alpha = round((alpha+0.05), 2)
print("AVGtime:", sum(tmp_list) / len(tmp_list))

# dbgList = []
# graphList = []
# pointer = target
# while pointer != source :
#     dbgList.append(pointer.index)
#     graphList.append(pointer)
#     pointer = pointer.predecessor
# dbgList.append(pointer.index)
# dbgList = reversed(dbgList)
# print(*dbgList, sep="->")