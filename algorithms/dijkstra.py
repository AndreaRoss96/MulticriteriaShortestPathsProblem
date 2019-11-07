from PriorityQueue import PriorityQueue

def dijkstraOneToAll(source):
    nodeSet = PriorityQueue()
    nodeSet.put(source, 0)
    # counter = 0
    while not nodeSet.isEmpty() :
        actualNode = nodeSet.getMin()
        # counter = counter + 1
        for nextNode, distance in actualNode.neighbors :
            newDistance = actualNode.minWeight + distance[0]
            if newDistance < nextNode.minWeight :
                #this is the better path, until now
                nextNode.minWeight = newDistance
                nextNode.predecessor = actualNode
                nodeSet.put(nextNode, newDistance)
                source.addShortestPath(nextNode, newDistance)   # all the path from the starting node are here
    # print("loops:", counter)
   


def dijkstraOneToOne(graph, source, target):
    nodeSet = list()
    nodeSet.extend(graph)
    while len(nodeSet) > 0 :
        actualNode = min(nodeSet, key=lambda elem: elem.minWeight)
        actualNode.visited = True

        if target.visited :
            break

        nodeSet.remove(actualNode)
        for nextNode, distance in actualNode.neighbors:
            newDistance = actualNode.minWeight + distance[0]
            if newDistance < nextNode.minWeight:
                nextNode.minWeight = newDistance
                nextNode.predecessor = actualNode
    if not target.visited:  # if the target is not been visited, it means that it wasn't in the set
        print("ERROR! impossible to reach the target")


def dijkstraListOfCandidate(source, target):
    listOfCand = PriorityQueue()
    listOfCand.put(source, 0)
    while not listOfCand.isEmpty() :
        actualNode = listOfCand.getMin()
        actualNode.visited = True

        if target.visited :
            break

        for nextNode, distance in actualNode.neighbors :
            newDistance = actualNode.minWeight + distance[0]
            if newDistance < nextNode.minWeight :
                nextNode.minWeight = newDistance
                nextNode.predecessor = actualNode 
                listOfCand.put(nextNode, newDistance)

    if not target.visited:  # if the target is not been visited, it means that it wasn't in the set
        print("ERROR! impossible to reach the target")
    # print("loops:", counter)
