
"""
Initialising all the the nodes for the dijkstra algorithm

@param graph
        the set of all nodes

@param startingNode
        the starting node
"""


def _initSingleNode(graph, source):
    for v in graph:
        v.reset()  # reset the value of predecessor, visited and minDistance of all nodes
    source.minDistance = 0
    source.visited = True
    return graph


def dijkstraOneToAll(graph, source):
    nodeSet = _initSingleNode(graph, source)
    while (len(nodeSet) > 0):
        actualNode = min(nodeSet, key=lambda elem: elem.minDistance)
        nodeSet.remove(actualNode)
        for nextNode, distance in actualNode.neighbors.items():
            tmp = actualNode.minDistance + distance
            if tmp < nextNode.minDistance:
                nextNode.minDistance = tmp
                nextNode.predecessor = actualNode
                # all the path from the starting node are here
                source.addShortestPath(nextNode, tmp)


def dijkstraOneToOne(graph, source, target):
    nodeSet = _initSingleNode(graph, source)
    while (len(nodeSet) > 0) or (target.visited == True):
        actualNode = min(nodeSet, key=lambda elem: elem.minDistance)
        nodeSet.remove(actualNode)
        for nextNode, distance in actualNode.neighbors.items():
            tmp = actualNode.minDistance + distance
            if tmp < nextNode.minDistance:
                nextNode.minDistance = tmp
                nextNode.predecessor = actualNode
                # source.addShortestPath(nextNode, tmp) #all the path from the starting node are here
    if not target.visited :  # if the target is not been visited, it means that it wasn't in the set
        print("ERROR! the target is not in the list!")


def dijkstraListOfCandidate(graph, source, target):
    _initSingleNode(graph, source)
    listOfCand = [source.neighbors.key()]
    print("List of candidate of the", source.index, "node:", listOfCand)
    while len(listOfCand) > 0:
        actualNode = min(listOfCand, key=lambda elem: elem.minDistance)
        actualNode.visited = True
        listOfCand.remove(actualNode)
        for nextNode, distance in actualNode.neighbors.items():
            tmp = actualNode.minDistance + distance
            if tmp < nextNode.minDistance:
                nextNode.minDistance = tmp
                nextNode.predecessor = actualNode
                for elem in nextNode.neighbors.key():
                    if not elem.visited :
                        listOfCand.append(elem)


""" 
Tutti gli algoritmi, in particolare quest'ultimo sono molto più efficaci
se si utilizzano delle strutture dati con priorità secondo me (che saresti te)
ad esempio list of candidate risparmi tempo se le metti in fila e fai pop all'inizio
invece di fare il foreach e il min su actualNode

Ho deciso di utilizzare la libreria di heapq, la quale implementa un classico binary heap, 
invece di implementare una Fibonacci heap, perché nell'estrazione del minore 
--> https://github.com/danielborowski/fibonacci-heap-python
"""
