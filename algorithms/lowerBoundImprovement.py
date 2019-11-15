from PriorityQueue import PriorityQueue
from bicriteriaDijkstra import binarySearchDijkBiCr
from bicriteriaDijkstra import dijkstraBiCrit
from utilities import initSingleNode, labelToString, isDominated

def __dijkstraBiCrit(source, target, alpha) :
    """
    With the bicriteria algorithm I decided to use the attribute "distance"
    of the node, because "minWeight" is used has comparator.
    Also in normal dijkstra is calcolated the weight, in this specific case we know
    that the "weights" are distance and danger 

    alpha : to varying of this variable the algorithm can find different results
                more α is near to 0, will be found the safest path
                more α is near to 1, will be found the shortest path
    """
    visitedNodes = []

    listOfCandidate = PriorityQueue()
    listOfCandidate.put(source, 0)
    while not listOfCandidate.isEmpty() :
        actualNode = listOfCandidate.getMin()
        actualNode.visited = True
        visitedNodes.append(actualNode)

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
                if not isDominated((nextNode.distance, nextNode.danger), nextNode.bests) :
                    for label in nextNode.bests :
                        if label[0] > nextNode.distance and label[1] >= nextNode.danger :
                            nextNode.bests.remove(label)
                    nextNode.bests.append((nextNode.distance, nextNode.danger))
                if alpha == 0 :         # Those ifs are useful only with the lowerBound Algorithm ()
                    if nextNode.bestLabel[1] is None or nextNode.bestLabel[1] > nextNode.danger :
                        nextNode.bestLabel[1] = nextNode.danger
                elif alpha == 1 :
                    if nextNode.bestLabel[0] is None or nextNode.bestLabel[0] > nextNode.distance :
                        nextNode.bestLabel[0] = nextNode.distance
    return visitedNodes


def lowerBoundImprovementReversed(source, target) :
    visitedNodes = __dijkstraBiCrit(source, target, 0) # safest path
    bestDanger = target.danger
    for v in visitedNodes:
        v.resetValue(True)
    __dijkstraBiCrit(source, target, 1) # shortest path
    bestDistance = target.distance

    labelQueue = PriorityQueue()
    sourceLabel = (0, 0, source, None, 0, None)
    source.labelList.append(sourceLabel)
    labelQueue.put(sourceLabel, sourceLabel[0])
    counter = 0
    while not labelQueue.isEmpty() :
        counter += 1
        actualLabel = labelQueue.getMin()
        distSoFar = actualLabel[0]
        dangSoFar = actualLabel[1]
        actualNode = actualLabel[2]
        parentIndex = actualLabel[4]
        
        for nearNode, weight in actualNode.neighbors :
            distance, danger = weight
            ownIndex = len(nearNode.labelList)
            newLabel = (distSoFar + distance, dangSoFar + danger, nearNode, actualNode, ownIndex, parentIndex) # creating of a new label
            # useLabel = True

            if isDominated(newLabel, nearNode.bests) :
                continue

            if nearNode.bestLabel[0] is not None and nearNode.bestLabel[1] is not None :    # if the best label is present, enter
                checkDistance = newLabel[0] + nearNode.bestLabel[0]
                checkDanger = newLabel[1] + nearNode.bestLabel[1]
                if checkDanger >= bestDanger and checkDistance >= bestDistance :  # if the values are negative is useless to check
                    continue # if new label is stupid continue for another loop
                else :
                    checkLabel = newLabel   
            else :
                checkLabel = newLabel

            if isDominated(checkLabel, target.labelList) : # if the newlabel + bestLabel is dominated is useless go on                
                continue # restart 'for' loop with another nearNode
            ####NEW PART####
            # else :
            #     nearNode.labelList.append(newLabel)
            #     if nearNode != target :
            #         labelQueue.put(newLabel, newLabel[0])

            useLabel = True
            for label in nearNode.labelList :
                if isDominated(newLabel, [label]) :
                    useLabel = False
                    break
            if useLabel :
                nearNode.labelList.append(newLabel)
                if nearNode != target :
                    labelQueue.put(newLabel, newLabel[0])        
    return counter


# def __isDominated(newLabel, labelList) :
#     """
#     If the label is already dominated by a label in the labelList
#     return True
#     else
#     return False
#     """
#     for oldLabel in labelList :
#         if newLabel[0] >= oldLabel[0] and newLabel[1] >= oldLabel[1] :
#             return True
#     return False