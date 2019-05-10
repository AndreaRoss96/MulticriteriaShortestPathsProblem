from PriorityQueue import PriorityQueue
from bicriteriaDijkstra import binarySearchDijkBiCr
from utilities import initSingleNode

def labelSettingAlgorithm(source, target) :
    """
    label = (dist, danger, owner, predecessor, index)
              [0]    [1]    [2]       [3]       [4]
    Step 0 :
        create first label (0, 0, source, null)
        and put it in the labelSet (a priorityQueue)
    Step 1 :
        if labelSet.empty() -> step 4
        else select the label w/ the less distance and calc the label of the neighbors
        NO -> (if the current label == target -> step 4)
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
    """
    labelQueue = PriorityQueue()
    sourceLabel = (0, 0, source, None, 0)
    source.labelList.append(sourceLabel)
    labelQueue.put(sourceLabel, sourceLabel[0])
    ending = False  # become True when a "nextNode" is equal to the target
    while not labelQueue.empty() :
        actualLabel = labelQueue.getMin()
        distSoFar = actualLabel[0]
        dangSoFar = actualLabel[1]
        actualNode = actualLabel[2]
        index = len(actualNode.labelList) - 1
        
        for nextNode, weight in actualNode.neighbors :
            distance, danger = weight
            newLabel = (distSoFar + distance, dangSoFar + danger, nextNode, actualNode, index) # creating of a new label
            useLabel = True

            if ending :
                if __isDominated(newLabel, target.labelList) :
                    break

            for label in nextNode.labelList :
                if not __usableLabel(newLabel, label, nextNode.labelList) :
                    useLabel = False
                    break # if a value is useless (1st case) the loop - label in labelList - is interrupt, to jump some loops
            if useLabel :
                nextNode.labelList.append(newLabel)
                if nextNode != target :
                    labelQueue.put(newLabel, newLabel[0])
                else :
                    ending = True


def __usableLabel(newLabel, oldLabel, labelsList) :
    if oldLabel[3] == None :
        return True
    if newLabel[0] >= oldLabel[0] and newLabel[1] >= oldLabel[1] :  # 1st case, this label is useless
        return False
    elif newLabel[0] < oldLabel[0] and newLabel[1] < oldLabel[1] :  # 2nd case, this label dominate a label
        labelsList.remove(oldLabel)
    return True                                                     # 3rd case, this label can't/isn't dominate/d

def __isDominated(newLabel, labelList) :
    """
    If the label is already dominated by a label in the target node
    return True
    else
    return False
    """
    for oldLabel in labelList :
        if newLabel[0] > oldLabel[0] and newLabel[1] > oldLabel[1] :
            return True
    return False

def lowerBoundImprovement(graph, source, target) :
    preprocessing = binarySearchDijkBiCr(graph, source, target)
    initSingleNode(graph, source)
    for distdang in preprocessing.keys() :
        target.labelList.append((distdang[0], distdang[1], target, None, None))
    # print(target.labelList)
    labelSettingAlgorithm(source, target)
    # print(target.labelList)
    for _ in range(0, len(preprocessing)) : 
        target.labelList.pop(0)
    


