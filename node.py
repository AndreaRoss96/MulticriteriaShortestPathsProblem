import sys

class Node(object):
    """
    The current vertex represent a vertex of the graph
    """

    def __init__(self, index, longitude, latitude):
        self.index = index                  #the index of the node
        self.longitude = longitude          
        self.latitude = latitude
       #TO DO --> X & Y
        self.x = "latitude"                 #x and y are coordinates derivates by the alt & long
        self.y = "longitude"
        self.neighbors = {}                 #dictionary with K->node & value->distance beetween two node next eachother
        self.visited = False                #to know if the node is already been visited
        self.predecessor = None             #the predecessor of this one node
        self.minDistance = sys.maxsize      #distance from the previous node
        self.shortestPaths = {}             #dictonary with K->node & value->total distance from the starting node

    """
    Reset the node
    """
    def reset(self):
        self.predecessor = None
        self.visited = False
        self.minDistance = sys.maxsize

    """ 
    Neighbors is a dictionary with:
    @param newNeighbor -> Key -> the next node
    @param info -> Value -> the weight of the arch (in the bicriteria version it will contains also the danger)
    """
    def addNeighbor(self, newNeighbor, info):
        self.neighbors.update(newNeighbor, info[0])
    
    """
    shortestPaths is a dictonary with:
    Key -> the destination node
    Value -> the total weight of all arches -> then also the danger
    """
    def addShortestPath(self, destination, totalWeight):
        # print("destination:", destination.index, "\n- total weight:", totalWeight)
       self.shortestPaths[destination] = totalWeight

    """
    Update the predecessor of the current node
    """
    def updatePredecessor(self, predecessor):
        self.predecessor = predecessor

    