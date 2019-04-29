from PriorityQueue import PriorityQueue

def dijkstraBiCrit(graph, source, target, alpha) :
    """
    With the bicriteria algorithm I decided to use the attribute "distance"
    of the node, because "minWeight" is used has comparator.
    Also in normal dijkstra is calcolated the weight, in this specific case we know
    that the "weights" are distance and danger 

    alpha : to varying of this variable the algorithm can find different results
                more α is near to 0, will be found the less dangerous path
                more α is near to 1, will be found the shortest path
    """
    listOfCandidate = PriorityQueue()
    listOfCandidate.put(source, 0)
    while not listOfCandidate.empty() :
        actualNode = listOfCandidate.getMin()
        actualNode.visited = True

        if target.visited :
            break

        for nextNode, weight in actualNode.neighbors : 
            distance, danger = weight
            weightResult = alpha*distance + (1-alpha)*danger
            newWeight = actualNode.minWeight + weightResult
            if newWeight < nextNode.minWeight :
                nextNode.minWeight = newWeight
                nextNode.distance = actualNode.distance + distance
                nextNode.danger = actualNode.danger + danger
                nextNode.predecessor = actualNode
                listOfCandidate.put(nextNode, newWeight)
