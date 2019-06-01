from Node import Node
from setup import graphBuilder
import time
import random 
import pandas as pds

dataN = pds.read_csv('graphs/berlin_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/berlin_arcs.csv', sep='\t', header=None)


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
"""
#default = 2000->2689
"""
take snap of
Paris 2070->15426
Paris 2000->2689
Berlin 1000->1510
also in bicriteria

"""
source = graph[1000]
target = graph[1510]


########## ONE -> ALL ##########
print("*"*40, "ONE TO ALL", "*"*40)
initSingleNode(graph, source)

start = time.time()
dijkstraOneToAll(source)
end = time.time()

print("time:", end-start)
print("from", source.index, "to", target.index, "the weight of the path is:", source.shortestPaths.get(target))

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

################################
########## ONE -> ONE ##########

print("*"*40, "ONE TO ONE", "*"*40)
initSingleNode(graph, source)

start = time.time()
# dijkstraOneToOne(graph, source, target)
end = time.time()

print("time:", end-start)
print("from",source.index, "to", target.index, "the weight of the path is:", target.minWeight)

######################
#### BACKTRACKING ####
######################
# dbgList = []
# pointer = target
# while pointer != source :
#     dbgList.append(pointer.index)
#     pointer = pointer.predecessor
# dbgList.append(target.index)
# dbgList = reversed(dbgList)
# print(*dbgList, sep="->")

################################
###### LIST OF CANDIDATE #######
print("*"*40, "LIST OF CANDIDATE", "*"*40)
initSingleNode(graph, source)

start = time.time()
dijkstraListOfCandidate(source, target)
end = time.time()

print("time:", end-start)
print("from",source.index, "to", target.index, "the weight of the path is:", target.minWeight)

######################
#### BACKTRACKING ####
######################
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

plotGraph(graph, reversed(graphList), "list of candidate", source, target)


############################
########## A STAR ##########
print("*"*40, "A STAR", "*"*40)
initSingleNode(graph, source)

start = time.time()
a_star(source, target)
end = time.time()

print("time:", end-start)
print("from",source.index, "to", target.index, "the weight of the path is:", target.minWeight)

######################
#### BACKTRACKING ####
######################
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

plotGraph(graph, reversed(graphList), "A_Star", source, target)