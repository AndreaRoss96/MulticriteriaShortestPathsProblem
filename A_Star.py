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
    print("printing LOC: ****")
    listone = listOfCand.slef()
    for elem in listone:
        print("node:", elem.index)

    while not listOfCand.empty() :
        print("printing LOC:")
        for elem in listOfCand.slef():
            print("node:", elem.index)
        actualNode = listOfCand.getMin()
        actualNode.visited = True
        print("actual node:", actualNode.index)
        # for nextNode, distance in actualNode.neighbors.items():
        #     #tmp = sum(distance, euclideanDistance(nextNode, target))
        #     tmp = distance + euclideanDistance(nextNode, target)
        #     listOfCand.put(nextNode, tmp)
#to calculate only one time the radq to get the euclidean distance, i will check if the node is visited or less,
#in case it isn't visited I will calculate the euclidean distance and use them in the queue


def euclideanDistance(source, destination) :
    dist = [(a-b)**2 for a, b in zip([source.x, source.y], [destination.x, destination.y])]
    return math.sqrt(sum(dist))
    
    #la prestazione è stata cacolata da https://stackoverflow.com/questions/37794849/efficient-and-precise-calculation-of-the-euclidean-distance#