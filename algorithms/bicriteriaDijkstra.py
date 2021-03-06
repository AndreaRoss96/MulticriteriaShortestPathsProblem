from PriorityQueue import PriorityQueue
from utilities import initSingleNode

def dijkstraBiCrit(source, target, alpha) :
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
                if alpha == 0 :         # Those ifs are useful only with the lowerBound Algorithm ()
                    if nextNode.bestLabel[1] is None or nextNode.bestLabel[1] > nextNode.danger :
                        nextNode.bestLabel[1] = nextNode.danger
                elif alpha == 1 :
                    if nextNode.bestLabel[0] is None or nextNode.bestLabel[0] > nextNode.distance :
                        nextNode.bestLabel[0] = nextNode.distance
    return visitedNodes

def dijkstraBiCrIteration(graph, source, target, increaseVal) :
    """
    Search solution by incrementing the value of α, so at each incrementation ther will be an execution of
    bicriteria Dijkstra algorithm

    increaseVale : float
        Value between 0 and 1, that is used to increment the value of alpha, each iteration.
        smallest value = more accurate results, but more execution time

    @return
        None if increaseVal is incorrect

        listDistDang : {
            (dist, dang) : alpha
            (dist, dang) : alpha
            ...
        }
    """
    if increaseVal >= 1 or increaseVal <= 0 :
        print("Please, insert a number greater than 0, but smaller than 1")
        return None

    listDistDang = {}
    counter = 0
    alpha = 0
    ending = False


    while alpha <= 1 :
        counter += 1
        initSingleNode(graph, source)
        dijkstraBiCrit(source, target, alpha)

        distDang = (target.distance, target.danger)

        if distDang in list(listDistDang.keys()) :
            alpha += increaseVal
            if not ending and alpha >= 1 :
                alpha = 1
                ending = True
        else :
            listDistDang.update({distDang : alpha})
            alpha = alpha / 2
    return listDistDang


def binarySearchDijkBiCr(graph, source, target) : 
    """
    Search the solutions using Dijkstra Bicriteria algorithm, changing the value of α following a binary search algorihm

    Faster than the normal dijkstra iteration

    @return
        totList : {
            (dist, dang) : alpha
            (dist, dang) : alpha
            ...
         }
    """
    leftList = [] # store all results of α € [0, 0.5]
    rightList = [] # store all results of α € ]0.5, 0]

    totList = {} # [(distDang, alpha), ...]

    approx = 5 # value of approximations
    right = 1
    left = 0

    dijkstraBiCrit(source, target, right)
    res = (target.distance, target.danger)
    rightList.append(res)
    totList.update({res : right})

    initSingleNode(graph, source)
    dijkstraBiCrit(source, target, left)
    res = (target.distance, target.danger)
    leftList.append(res)
    totList.update({res : left})

    listDimension = None
    condition = True
    while condition : 
        alpha = (right - left) / 2
        tmp = str(alpha)
        alpha = float(tmp[:approx])
        if alpha > 0 :
            alpha = alpha + left
            initSingleNode(graph, source)
            dijkstraBiCrit(source, target, alpha)
            res = (target.distance, target.danger)

            if res in leftList :
                left = alpha
            elif res in rightList :
                right = alpha
            else :
                if res[0] < leftList[len(leftList) - 1][0] : # is res the lower than the lowest value in leftList
                    leftList.append(res)
                    totList.update({res : alpha})
                    right = alpha
                else:
                    rightList.append(res)
                    totList.update({res : alpha})
                    left = alpha
        else :
            if listDimension == len(totList) :
                condition = False
            else :
                listDimension = len(totList)
            right = 1
            left = 0
    return totList
