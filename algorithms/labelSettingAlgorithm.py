from PriorityQueue import PriorityQueue
from bicriteriaDijkstra import binarySearchDijkBiCr
from bicriteriaDijkstra import dijkstraBiCrit
from utilities import initSingleNode, labelToString, isDominated

def labelSettingAlgorithm(source, target) :
    """
    label = (dist, danger, owner, predecessor, ownerListPos, predListPos)
              [0]    [1]    [2]       [3]           [4]          [5]

              [ownerListPos] : is the position on the own label list
              [predListPos] : is the postion in the labelList of the predecessor label
    
    Step 0 :
        create first label (0, 0, source, null, 0, null)
        and put it in the labelSet (a priorityQueue)
    Step 1 :
        if labelSet.isEmpty() -> step 4
        else select the label w/ the less distance and calc the label of the neighbors
    Step 2 :
        foreach neighbor of the current label calc
            What to do when i found a new label for a node : - 3 possibility
                1st - new label IS DOMINATED by one already existence (in the node.labelList) -> delete new label
                2nd - new label DOMINATE one or more already existence ( " " ) -> delete old label, add new label
                3rd - new label ISN'T DOMINATED AND CAN'T DOMINATE any other node -> add new label
    Step 3 :
        return to Step 1
    Step 4:
        End

    @return
        number of loops
    """
    labelQueue = PriorityQueue()
    sourceLabel = (0, 0, source, None, 0, None)
    source.labelList.append(sourceLabel)
    labelQueue.put(sourceLabel, sourceLabel[0])
    ending = False  # become True when a "nearNode" is equal to the target
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
            useLabel = True

            if ending : # stop condition
                if isDominated(newLabel, target.labelList) :
                    continue # restart for loop if the new label is dominated

            for label in nearNode.labelList :
                if not __usableLabel(newLabel, label, nearNode.labelList) :
                    useLabel = False
                    break # if a value is useless (1st case) the loop - label in labelList - is interrupt, to jump some loops
            if useLabel :
                nearNode.labelList.append(newLabel)
                if nearNode != target :
                    labelQueue.put(newLabel, newLabel[0])
                else :
                    ending = True
    return counter

#RIMUOVERE usableLabel basta passare a __isDominated(newLabel, [label])
def __usableLabel(newLabel, oldLabel, labelsList) :
    if newLabel[0] >= oldLabel[0] and newLabel[1] >= oldLabel[1] :  # 1st case, this label is useless
        return False
    return True                                                     # 3rd case, this label can't/isn't dominate/d

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


###########################
# LOWER BOUND IMPROVEMENT #
###########################

def lowerBoundImprovement(graph, source, target) :
    """
    Evolution of the normal label-setting algorithm, with a preprocessing that uses
    Dijkstra bicriteria algorithm

    @return
        number of loops
    """
    visitedNodes = dijkstraBiCrit(source, target, 0) # safest path
    bestDanger = target.danger
    
    for v in visitedNodes:
        v.resetValue(True)  # reset the value of predecessor, visited and minWeight of all nodes
    # source.minWeight = 0 # ma a che servono ??
    # source.visited = True

    dijkstraBiCrit(source, target, 1) # shortest path
    bestDistance = target.distance

    labelQueue = PriorityQueue()
    sourceLabel = (0, 0, source, None, 0, None)
    source.labelList.append(sourceLabel)
    labelQueue.put(sourceLabel, sourceLabel[0])
    counter = 0
    while not labelQueue.isEmpty() :
        actualLabel = labelQueue.getMin()
        distSoFar = actualLabel[0]
        dangSoFar = actualLabel[1]
        actualNode = actualLabel[2]
        parentIndex = actualLabel[4]
        
        for nearNode, weight in actualNode.neighbors :
            distance, danger = weight
            ownIndex = len(nearNode.labelList)
            newLabel = (distSoFar + distance, dangSoFar + danger, nearNode, actualNode, ownIndex, parentIndex) # creating of a new label
            useLabel = True

            if nearNode.bestLabel[0] is not None and nearNode.bestLabel[1] is not None :    # if the best label is present, enter
                checkDistance = bestDistance - nearNode.bestLabel[0]
                checkDanger = bestDanger - nearNode.bestLabel[1]
                if checkDanger > 0 and checkDistance > 0 :  # if the values are negative is useless to check
                    checkLabel = (newLabel[0] + checkDistance, newLabel[1] + checkDanger)
                else :
                    checkLabel = newLabel   
            else :
                checkLabel = newLabel

            if isDominated(checkLabel, target.labelList) : # if the newlabel + bestLabel is dominated is useless go on                
                continue # restart 'for' loop with another nearNode
            
            for label in nearNode.labelList :
                if not __usableLabel(newLabel, label, nearNode.labelList) :
                    useLabel = False
                    break # if a value is useless (1st case) the loop - label in labelList - is interrupt, to jump some loops
            if useLabel :
                nearNode.labelList.append(newLabel)
                if nearNode != target :
                    labelQueue.put(newLabel, newLabel[0])
            counter += 1
    return counter



def lowerBoundImprovementTry(graph, source, target) :
    """
    Uses the label setting algorithm to find the paths, but with a dijkstra preprocessing
    """
    preprocessing = binarySearchDijkBiCr(graph, source, target)
    initSingleNode(graph, source)
    for distdang in preprocessing.keys() :
        target.labelList.append((distdang[0], distdang[1], target, None, None))
    labelSettingAlgorithm(source, target)
    for _ in range(0, len(preprocessing)) : 
        target.labelList.pop(0)
    

