from PriorityQueue import PriorityQueue

def labelSettingAlgorithm(source, target) :
    """
    label = (dist, danger, owner, predecessor)
              [0]    [1]    [2]       [3]
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
    sourceLabel = (0, 0, source, None)
    labelQueue.put(sourceLabel, sourceLabel[0])
    ending = False  # become True when a node is equal to the target
    while not labelQueue.empty() :
        actualLabel = labelQueue.getMin()
        distSoFar = actualLabel[0]
        dangSoFar = actualLabel[1]
        actualNode = actualLabel[2]

        if target == actualNode : # if is considered a node equal to target the loop will restarted
            ending = True
            continue
        
        for nextNode, weight in actualNode.neighbors :
            distance, danger = weight
            newLabel = (distSoFar + distance, dangSoFar + danger, nextNode, actualNode) # creating of a new label
            useLabel = True

            if ending :     # if ending is True (a label has reached the target), check if the current label is dominated
                restartWhile = False
                for label in target.labelList : 
                    if not __labelDoom(newLabel, label, target.labelList) : # if the actual label is dominated the while loop will restart
                        restartWhile = True
                        break
                if restartWhile :
                    break

            for label in nextNode.labelList :
                if not __labelDoom(newLabel, label, nextNode.labelList) :
                    useLabel = False
                    break # if a value is useless (1st case) the loop - label in labelList - is interrupt
            if useLabel :
                nextNode.labelList.append(newLabel)
                labelQueue.put(newLabel, newLabel[0])


def __labelDoom(newLabel, oldLabel, labelsList) :
    if newLabel[0] > oldLabel[0] and newLabel[1] > oldLabel[1] :    # 1st case, this label is useless
        return False
    elif newLabel[0] < oldLabel[0] and newLabel[1] < oldLabel[1] :  # 2nd case, this label dominate a label
        labelsList.remove(oldLabel)
    return True                                                     # 3rd case, this label can't/isn't dominate/d