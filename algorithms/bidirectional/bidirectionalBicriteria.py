from PriorityQueue import PriorityQueue
from utilities import labelToString

# directions
fw = True
bw = False
paretoList = []


def bidirectionalBicriteriaAlgorithm(source, target):
    """
    label = (dist, danger, owner, predecessor, ownerListPos, predListPos)
              [0]    [1]    [2]       [3]           [4]          [5]         
    --> the backward's labels work as the normals,
        but when the path has to be constructed it is possible to do a reverse backtracking

    paretoLabel = (dist, dang, owner, (fwPred, fwOwnerListPost, fwpredListPos), (bwPred, bwOwnerListPost, bwpredListPos))
    """
    forwardQueue = PriorityQueue()
    backwardQueue = PriorityQueue()

    queueContainer = {  # change direction each loop
        fw: forwardQueue,
        bw: backwardQueue
    }

    paretoList = []
    dir = False

    sourceLabel = (0, 0, source, None, 0, None)
    source.directedLabelList[fw].append(sourceLabel)
    forwardQueue.put(sourceLabel, sourceLabel[0])
    targetLabel = (0, 0, target, None, 0, None)
    target.directedLabelList[bw].append(targetLabel)
    backwardQueue.put(targetLabel, targetLabel[0])
    counter = 0
    # min(fw) + min(bw) have to be not dominated ## not __isDominated(*
    while __checkLoop(forwardQueue, backwardQueue):
    #while forwardQueue or backwardQueue :
        counter += 1
        # print("count:", counter)
        dir = __getDirection(dir)
        actualLabel = queueContainer.get(dir).getMin()
        distSoFar = actualLabel[0]
        dangSoFar = actualLabel[1]
        actualNode = actualLabel[2]
        parentIndex = actualLabel[4]

        for nearNode, weight in actualNode.neighbors:
            distance, danger = weight
            ownIndex = len(nearNode.directedLabelList[dir])
            newLabel = (distSoFar + distance, dangSoFar + danger,
                        nearNode, actualNode, ownIndex, parentIndex)

            if not __isDominated(newLabel, nearNode.directedLabelList[dir]):
                nearNode.directedLabelList[dir].append(newLabel)
                queueContainer[dir].put(newLabel, newLabel[0])#__getLexicographicMin(newLabel))
                # when a list is empty = FALSE
                if nearNode.directedLabelList[not dir]:
                    __combine(newLabel, nearNode.directedLabelList[not dir])
    return paretoList


def __checkLoop(fwQueue, bwQueue):
    tmpLabel = (fwQueue.minValue()[0] + bwQueue.minValue()[0], fwQueue.minValue()[1] + bwQueue.minValue()[1])
    # print("On checkloop:", paretoList)
    return not __isDominated(tmpLabel, paretoList)


def __isDominated(label, dominatorLabelList):
    # print("check on is dominated")
    # print(label)
    # print(dominatorLabelList)
    # if the list is empty step into  (empty = False)
    # if not dominatorLabelList:
    #     return False
    for dominatorLabel in dominatorLabelList:
        # print(dominatorLabel, dominatorLabel[0])
        # print(label, label[0], label[1])
        if label[0] >= dominatorLabel[0] and label[1] >= dominatorLabel[1]:
            return True
        # elif label[0] < dominatorLabel[0] and label[1] < dominatorLabel[1] :
        #     dominatorLabelList.remove(dominatorLabel)
    return False


def __combine(newLabel, nearLabelList):
    """
    combine forward and backward to create a paretoLabel

    paretoLabel = (dist, dang, owner, (fwPred, fwOwnerListPost, fwpredListPos), (bwPred, bwOwnerListPost, bwpredListPos))
    """
    # print("labels:", labelToString(newLabel))
    # nodeIndex = newLabel[2].index
    # if nodeIndex not in paretoList :
    #     print("pareto update")

    for nearLabel in nearLabelList:
        # print("fwLabel= newLabel:{0[0]} dang:{0[1]} index:{0[2].index} pred:{0[3].index}     ||  nearLabel= dist:{1[0]} dang:{1[1]} index:{1[2].index} pred:{1[3].index}".format(newLabel, nearLabel))
        dist = newLabel[0] + nearLabel[0]
        dang = newLabel[1] + nearLabel[1]
        fwInfo = newLabel[3:]
        bwInfo = nearLabel[3:]

        # created paretoLabel
        result = (dist, dang, newLabel[2], fwInfo, bwInfo)
        if not __isDominated(result, paretoList) :
            # print("result:", result[0], result[1])
            for paretoLabel in paretoList:
                if __isDominated(paretoLabel, [result]):
                    # print("Via dai balle")
                    paretoList.remove(paretoLabel)
            paretoList.append(result)


def __getDirection(direction):
    return not direction


def __getLexicographicMin(label) :
    return label[0] if label[0] <= label [1] else label[1]