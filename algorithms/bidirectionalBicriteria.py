from PriorityQueue import PriorityQueue

def bidirectionalBicriteriaAlgorithm(source, target) :
    """
    label = (dist, danger, owner, predecessor, ownerListPos, predListPos)
              [0]    [1]    [2]       [3]           [4]          [5]
    --> the backward's labels work as the normals,
        but when the path has to be constructed it is possible to do a reverse backtracking
    """
    forwardQueue = PriorityQueue()
    backwardQueue = PriorityQueue()
    dir = True
    queueContainer = {
        True : forwardQueue,
        False : backwardQueue
    }

    sourceLabel = (0, 0, source, None, 0, None)
    source.labelList.append(sourceLabel)
    forwardQueue.put(sourceLabel, sourceLabel[0])
    targetLabel = (0, 0, target, None, 0 , None)   
    target.labelList.append(targetLabel)
    backwardQueue.put(targetLabel, targetLabel[0])




def __isDominated(firstLabel, secondLabel, ) :


def __combine(forwardLabel, backwardLabel) :
    """
    combine forward and backward to 
    """