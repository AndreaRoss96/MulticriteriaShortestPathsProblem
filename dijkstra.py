
"""
Initialising all the the nodes for the dijkstra algorithm

graph : the set of all nodes

source : the starting node

target : target node

"""
from PriorityQueue import PriorityQueue

def initSingleNode(graph, source):
    for v in graph:
        v.resetValue()  # reset the value of predecessor, visited and minDistance of all nodes
    source.minDistance = 0
    source.visited = True
    return graph


def dijkstraOneToAll(graph, source):
    # nodeSet = list()
    # nodeSet.extend(initSingleNode(graph, source))
    #############################
    initSingleNode(graph, source)
    nodeSet = PriorityQueue()
    nodeSet.put(source, 0)
    #############################
    # while (len(nodeSet) > 0):
    while not nodeSet.empty() :
        # actualNode = min(nodeSet, key=lambda elem: elem.minDistance)
        # nodeSet.remove(actualNode)
        #############################
        actualNode = nodeSet.getMin()
       # print("actual",actualNode.index)
        #############################
        for nextNode, distance in actualNode.neighbors.items():
            tmp = actualNode.minDistance + distance
            if tmp < nextNode.minDistance :
                #this is the better path, until now
         #       print(nextNode.index)
                nextNode.minDistance = tmp
                nextNode.predecessor = actualNode
                nodeSet.put(nextNode, tmp)
                source.addShortestPath(nextNode, tmp)   # all the path from the starting node are here
   


def dijkstraOneToOne(graph, source, target):
    nodeSet = list()
    nodeSet.extend(initSingleNode(graph, source))
    while len(nodeSet) > 0 :
        actualNode = min(nodeSet, key=lambda elem: elem.minDistance)
        actualNode.visited = True

        if target.visited :
            break

        nodeSet.remove(actualNode)
#        print("actual node:", actualNode.index)
        for nextNode, distance in actualNode.neighbors.items():
            tmp = actualNode.minDistance + distance
            if tmp < nextNode.minDistance:
                nextNode.minDistance = tmp
                nextNode.predecessor = actualNode
                # source.addShortestPath(nextNode, tmp) #all the path from the starting node are here
    if not target.visited:  # if the target is not been visited, it means that it wasn't in the set
        print("ERROR! the target is not in the list!")


def dijkstraListOfCandidate(graph, source, target):
    initSingleNode(graph, source)
    listOfCand = PriorityQueue()
    # initSingleNode(graph, source)
    # listOfCand = set([source])
    listOfCand.put(source, 0)
    while not listOfCand.empty() :
        actualNode = listOfCand.getMin()
        # actualNode = min(listOfCand, key=lambda elem: elem.minDistance)
        # listOfCand.remove(actualNode)
#        print("actual node:", actualNode.index)
        actualNode.visited = True

        if target.visited :
            break

        for nextNode, distance in actualNode.neighbors.items():
            if not nextNode.visited :
                tmp = actualNode.minDistance + distance
                if tmp < nextNode.minDistance:
                    nextNode.minDistance = tmp
                    nextNode.predecessor = actualNode    
                    # listOfCand.add(nextNode)
                    listOfCand.put(nextNode, tmp)
#TODO: retry test with a lot of nodes


""" 
Ho deciso di utilizzare la libreria di heapq, la quale implementa un classico binary heap, 
invece di implementare una Fibonacci heap, perché nell'estrazione del minore 
--> https://github.com/danielborowski/fibonacci-heap-python
"""
