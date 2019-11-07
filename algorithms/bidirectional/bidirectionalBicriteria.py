from PriorityQueue import PriorityQueue
from utilities import labelToString
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
    counter = 0
    while not __isDominated(*__checkLoop(forwardQueue, backwardQueue)) : # min(fw) + min(bw) have to be not dominated
        counter += 1
        dir = __getDirection(dir)
        actualLabel = queueContainer.get(dir).getMin()
        distSoFar = actualLabel[0]
        dangSoFar = actualLabel[1]
        actualNode = actualLabel[2]
        parentIndex = actualLabel[4]
        
        for nearNode, weight in actualNode.neighbors :
            distance, danger = weight
            ownIndex = len(nearNode.directedLabelList[dir])
            newLabel = (distSoFar + distance, dangSoFar + danger, nearNode, actualNode, ownIndex, parentIndex)

            if not __isDominated(newLabel, nearNode.directedLabelList[dir]) :
                nearNode.directedLabelList[dir].append(newLabel)
                queueContainer[dir].put(newLabel, newLabel[0])
                if nearNode.directedLabelList[not dir] : # when a list is empty = FALSE
                    __combine(newLabel, nearNode.directedLabelList[not dir])

    

def __checkLoop(fwQueue, bwQueue) :
    tmpLabel = (fwQueue.minValue()[0] + bwQueue.minValue()[0], fwQueue.minValue()[1] + bwQueue.minValue()[1])
    tmpList = list(paretoList.values())
    print("On checkloop:", tmpList)
    return (tmpLabel, tmpList)


def __isDominated(label, dominatorLabelList) :
    # print("check on is dominated")
    # print(label)
    # print(dominatorLabelList)
    for dominatorLabel in dominatorLabelList :
        print(dominatorLabel, dominatorLabel[0], dominatorLabel[1])
        print(label, label[0], label[1])
        if dominatorLabel[0] >= label[0] and dominatorLabel[1] >= label[1] :
            return False
        return True 


def __combine(newLabel, nearLabelList) :
    """
    combine forward and backward to create a paretoLabel

    paretoLabel = (dist, dang, owner, (fwPred, fwOwnerListPost, fwpredListPos), (bwPred, bwOwnerListPost, bwpredListPos))
    """
    print("labels:", labelToString(newLabel))
    nodeIndex = newLabel[2].index
    if nodeIndex not in paretoList :
        paretoList.update({nodeIndex : []}) # create a new place in th dictionary

    for nearLabel in nearLabelList :
        print("fwLabel= newLabel:{0[0]} dang:{0[1]} pred:{0[3].index}     ||  nearLabel= dist:{1[0]} dang:{1[1]} pred:{1[3].index}".format(newLabel, nearLabel))
        dist = newLabel[0] + nearLabel[0]
        dang = newLabel[1] + nearLabel[1]
        fwInfo = newLabel[3:]
        bwInfo = nearLabel[3:]
        
        result = (dist, dang, fwInfo, bwInfo) # created paretoLabel
        paretoList.get(nodeIndex).append(result)


def __getDirection(direction) :
    return not direction