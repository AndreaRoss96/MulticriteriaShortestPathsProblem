from PriorityQueue import PriorityQueue

"""
Faccio un paretoList dove ci metto tutte le soluzioni, poi tutti i nodi
avranno i loro label e le info per il backtracking
"""

#directions
fw = True
bw = False
paretoList = {}

def bidirectionalBicriteriaAlgorithm(source, target) :
    """
    label = (dist, danger, owner, predecessor, ownerListPos, predListPos)
              [0]    [1]    [2]       [3]           [4]          [5]         
    --> the backward's labels work as the normals,
        but when the path has to be constructed it is possible to do a reverse backtracking

    paretoLabel = (dist, dang, owner, (fwPred, fwOwnerListPost, fwpredListPos), (bwPred, bwOwnerListPost, bwpredListPos))
    """
    forwardQueue = PriorityQueue()
    backwardQueue = PriorityQueue()

    queueContainer = { # change direction each loop
        fw : forwardQueue,
        bw : backwardQueue
    }

    dir = bw

    sourceLabel = (0, 0, source, None, 0, None)
    source.labelList.append(sourceLabel)
    forwardQueue.put(sourceLabel, sourceLabel[0])
    targetLabel = (0, 0, target, None, 0, None)   
    target.labelList.append(targetLabel)
    backwardQueue.put(targetLabel, targetLabel[0])
    while not __isDominated(*__controlLoop(forwardQueue, backwardQueue)) : # min(fw) + min(bw) have to be not dominated
        dir = not dir
        actualLabel = queueContainer.get(dir).getMin()
        #il resto è storia
    

def __controlLoop(fwQueue, bwQueue) :
    tmpLabel = (fwQueue.minValue()[0] + bwQueue.minValue()[0],
        fwQueue.minValue()[1] + bwQueue.minValue()[1])
    tmpList = list(paretoList.values())
    return (tmpLabel, tmpList)


def __isDominated(label, dominatorLabelList) :
    for dominatorLabel in dominatorLabelList :
        if dominatorLabel[0] >= label[0] and dominatorLabel[1] >= label[1] :
            return False
        return True 


def __combine(forwardLabel, backwardLabel) :
    """
    combine forward and backward to create a paretoLabel

    paretoLabel = (dist, dang, owner, (fwPred, fwOwnerListPost, fwpredListPos), (bwPred, bwOwnerListPost, bwpredListPos))
    """
    nodeIndex = forwardLabel[2].index
    paretoList.update({nodeIndex : []}) # create a new place in th dictionary
    for fwLabel in forwardLabel[2].directedLabelList[fw] :
        for bwLabel in backwardLabel[2].directedLabelList[bw] :
            dist = fwLabel[0] + bwLabel[0]
            dang = fwLabel[1] + bwLabel[1]
            fwInfo = forwardLabel[3:]
            bwInfo = backwardLabel[3:]
            
            result = (dist, dang, fwInfo, bwInfo) # created paretoLabel
            paretoList.get(nodeIndex).append(result)


def __getDirection(direction) :
    return not direction