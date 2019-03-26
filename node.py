import sys


class Node(object):
    """
    The current vertex represent a vertex of the graph
    """

    def __init__(self, index, latitude, longitude):
        self.index = index  # the index of the node
        self.longitude = longitude
        self.latitude = latitude
        self.y = longitude
        self.x = latitude
       # TO DO --> X & Y
        # self.x = "latitude"                 #x and y are coordinates derivates by the alt & long
        # self.y = "longitude"
        # dictionary with K->node & value->distance beetween two node next eachother
        self.neighbors = {}
        self.visited = False  # to know if the node is already been visited
        self.predecessor = None  # the predecessor of this one node
        self.minDistance = sys.maxsize  # distance from the previous node
        # dictonary with K->node & value->total distance from the starting node
        self.shortestPaths = {}
        self.euclidean = None  # Used in the A* algorithm to limitate the utilisation of sqrt

    def resetValue(self):
        """
        Reset the node
        """
        self.predecessor = None
        self.visited = False
        self.minDistance = sys.maxsize
        self.upToDate = False

    def addNeighbor(self, newNeighbor, info):
        """ 
        Neighbors is a dictionary with:
        @param newNeighbor -> Key -> the next node
        @param info -> Value -> the weight of the arch (in the bicriteria version it will contains also the danger)
        """
        self.neighbors.update(newNeighbor, info[0])
    
    def addShortestPath(self, destination, totalWeight):
        """
        shortestPaths is a dictonary with:
        Key -> the destination node
        Value -> the total weight of all arches -> then also the danger
        """
        self.shortestPaths[destination] = totalWeight

    def updatePredecessor(self, predecessor):
        """
        Update the predecessor of the current node
        """
        self.predecessor = predecessor

    def __lt__(self, other):
        return self.index < other.index

    
