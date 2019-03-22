
"""
Initialising all the the nodes for the dijkstra algorithm

@param graph
        the set of all nodes

@param startingNode
        the starting node
"""


def initSingleNode(graph, source):
    print("inizializzo")
    for v in graph:
        v.resetValue()  # reset the value of predecessor, visited and minDistance of all nodes
    source.minDistance = 0
    source.visited = True
    return graph


def dijkstraOneToAll(graph, source):
    nodeSet = list()
    nodeSet.extend(initSingleNode(graph, source))
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
    nodeSet = list()
    nodeSet.extend(initSingleNode(graph, source))
    while (len(nodeSet) > 0) :
        actualNode = min(nodeSet, key=lambda elem: elem.minDistance)
        actualNode.visited = True
        nodeSet.remove(actualNode)
        print("actual node:", actualNode.index)
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
    listOfCand = set(source.neighbors.keys())
    print("List of candidate of the", source.index)
    while len(listOfCand) > 0:

        print("printing LOC:")
        for elem in listOfCand:
            print("node:", elem.index)
        actualNode = min(listOfCand, key=lambda elem: elem.minDistance)
        print("actual node:", actualNode.index)
        actualNode.visited = True
        listOfCand.remove(actualNode)
        for nextNode, distance in actualNode.neighbors.items():
            tmp = actualNode.minDistance + distance
            if tmp < nextNode.minDistance:
                nextNode.minDistance = tmp
                nextNode.predecessor = actualNode    
            if not nextNode.visited :
                listOfCand.add(nextNode)
#riguarda l'algoritmo, problema con i vicini 
#se ad esmpio vado nel nodo 2 dopo non mi accorgo che il 4 non è vantaggioso
        if target.visited :
            print ("maledetto dio")
            break


""" 
Tutti gli algoritmi, in particolare quest'ultimo sono molto più efficaci
se si utilizzano delle strutture dati con priorità secondo me (che saresti te)
ad esempio list of candidate risparmi tempo se le metti in fila e fai pop all'inizio
invece di fare il foreach e il min su actualNode

Ho deciso di utilizzare la libreria di heapq, la quale implementa un classico binary heap, 
invece di implementare una Fibonacci heap, perché nell'estrazione del minore 
--> https://github.com/danielborowski/fibonacci-heap-python
"""
