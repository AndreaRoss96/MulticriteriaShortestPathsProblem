"""
The A Star algorithm (or ‘A*’) can be considered an extension of Dijkstra’s
algorithm, because it achieves better performance and accuracy by using
heuristics. A*, to determinate how to extend its paths to the target, needs
to minimizes this equation:
    f(n) = g(n)+h(n)
    
• n is the next path’s node
• g(n) is path’s cost from the beginning to n
• h(n) is the heuristic function
"""
import math
from PriorityQueue import PriorityQueue

def a_star(source, target) :
    listOfCand = PriorityQueue()
    listOfCand.put(source, 0)

    counter = 0

    while not listOfCand.isEmpty() :
        actualNode = listOfCand.getMin()
        counter = counter + 1
        actualNode.visited = True

        if target.visited :
            break

        for nextNode, distance in actualNode.neighbors :  
            if not nextNode.visited :   

                newDistance = actualNode.minWeight + distance[0]
                
                if newDistance < nextNode.minWeight :
                    #this path is the best until now, let's record
                    if nextNode.euclidean is None : # this check is to minimazie the calculation of the "euclidean distance"
                        nextNode.euclidean = euclideanDistance(nextNode, target)
                    
                    nextNode.minWeight = newDistance
                    nextNode.predecessor = actualNode
                    priority = newDistance + nextNode.euclidean
                    listOfCand.put(nextNode, priority)
    print("loops:", counter)


def euclideanDistance(source, destination) :
    dist = [(a-b)**2 for a, b in zip([source.x, source.y], [destination.x, destination.y])]
    res = math.sqrt(sum(dist))
    return res

    #performance calculated https://stackoverflow.com/questions/37794849/efficient-and-precise-calculation-of-the-euclidean-distance#