"""
The A* algorithm is similar to dijkstra algorithm
but it enjoys a better performance and accuracy.
In fact this algort

***
Guarda nell'agenda, quello da scrivere è perfettamente riportato
"""
import math
from dijkstra import initSingleNode
from PriorityQueue import PriorityQueue

def a_star(graph, source, target) :
    initSingleNode(graph, source)
    listOfCand = PriorityQueue()
    listOfCand.put(source, 0)

    counter = 0

    while not listOfCand.empty() :
        actualNode = listOfCand.getMin()
        counter = counter + 1
        actualNode.visited = True
        if target.visited :
            break

        for nextNode, distance in actualNode.neighbors.items():

            if not nextNode.visited :
                #to calculate only one time the radq to get the euclidean distance, i will check if the node is visited or less,
                #in case it isn't visited I will calculate the euclidean distance and use them in the queue
                if nextNode.euclidean == None :
                    nextNode.euclidean = euclideanDistance(nextNode, target)

                tmp = actualNode.distance + distance + nextNode.euclidean
                
                if tmp < nextNode.minDistance :
                    #this path is the best until now, let's record
                    nextNode.minDistance = tmp
                    nextNode.distance = tmp - nextNode.euclidean
                    nextNode.predecessor = actualNode
                    listOfCand.put(nextNode, tmp)
    print("loops:", counter)


def euclideanDistance(source, destination) :
    dist = [(a-b)**2 for a, b in zip([source.x, source.y], [destination.x, destination.y])]
    # res = math.sqrt(sum(dist)) --> the square root is unnecessary
    return sum(dist)
    
    #la prestazione è stata cacolata da https://stackoverflow.com/questions/37794849/efficient-and-precise-calculation-of-the-euclidean-distance#