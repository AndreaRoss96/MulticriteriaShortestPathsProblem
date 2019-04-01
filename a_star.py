"""
The A* algorithm is similar to dijkstra algorithm
but it enjoys a better performance and accuracy.
In fact this algort

***
Guarda nell'agenda, quello da scrivere è perfettamente riportato
"""
import math
from PriorityQueue import PriorityQueue

def a_star(graph, source, target) :
    listOfCand = PriorityQueue()
    listOfCand.put(source, 0)

    counter = 0

    while not listOfCand.empty() :
        actualNode = listOfCand.getMin()
        counter = counter + 1
        actualNode.visited = True

        if target.visited :
            break

        for nextNode, distance in actualNode.neighbors :  
            if not nextNode.visited :   

                newDistance = actualNode.minDistance + distance
                
                if newDistance < nextNode.minDistance :
                    #this path is the best until now, let's record
                    if nextNode.euclidean is None : # this check is to minimazie the calculation of the "euclidean distance"
                        nextNode.euclidean = euclideanDistance(nextNode, target)
                    
                    nextNode.minDistance = newDistance
                    nextNode.predecessor = actualNode
                    priority = newDistance + nextNode.euclidean
                    listOfCand.put(nextNode, priority)
    print("loops:", counter)


def euclideanDistance(source, destination) :
    dist = [(a-b)**2 for a, b in zip([source.x, source.y], [destination.x, destination.y])]
    res = math.sqrt(sum(dist))
    return res

    #la prestazione è stata cacolata da https://stackoverflow.com/questions/37794849/efficient-and-precise-calculation-of-the-euclidean-distance#