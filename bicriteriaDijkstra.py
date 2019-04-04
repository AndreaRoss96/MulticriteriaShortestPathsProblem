from PriorityQueue import PriorityQueue

def dijkstraBiCrit(graph, source, target, alpha) :
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
