import sys
from utilities import wgsToEcef

class Node(object):
    """
    The current vertex represent a vertex of the graph
    
    index : the index of the node
    longitude, latitude : geographical coordinates of the node
    x, y : cartesian coordinates of the node
    neighbors : list of tuples with [(K, value), (K, value), ...], where: K->node & value->[distance, danger] beetween two node next eachother
    visited : false if the node has not been visited, true otherwise
    predecessor : the node predecessor of this node
    minWeight : the total weight from the source node
    
    shortestPaths : dictonary with K->node & value->total distance from this node | used in oneToAll
    
    euclidean : misure the euclidean distance of the current node from the target | used in A* algorithm

    || Bicriteria uses
    distance : the distance from the source
    danger : total danger from the source

    || Label setting algorithm uses
    labelList : a list of all labels (not dominated), used to store information during the building of the paths [(dist, danger, owner, predecessor, listPosition, predListPos), (di, da, ow, pr, lp, plp), .... , (...)]
    --> all nodes will have a list of similar label with different predecessor, index ecc... 
    """

    def __init__(self, index, longitude, latitude):
        self.index = int(index)  # the index of the node
        self.longitude = longitude
        self.latitude = latitude
        self.x, self.y = wgsToEcef(latitude, longitude)
        self.neighbors = []  
        self.visited = False 
        self.predecessor = None
        self.minWeight = sys.maxsize
        self.shortestPaths = {} 

        self.euclidean = None

        self.distance = 0
        self.danger = 0

        self.labelList = []

        self.bestLabel = [None, None]

        fwLabelList = [] # forward labelList
        bwLabelList = [] # backward labelList
        self.directedLabelList = {
            True : fwLabelList,
            False : bwLabelList
        }

        self.bests = []
        self.bestDistanceLabel = None
        self.bestDangerLabel = None

           
    def resetValue(self, needBestLabel) :
        """
        Reset the node

        needBestLabel : Bool
            false if you need to reset bestLabel, True otherwise
        """
        self.predecessor = None
        self.visited = False
        self.minWeight = sys.maxsize
        self.upToDate = False
        self.euclidean = None
        self.distance = 0
        self.danger = 0
        self.labelList = []
        self.shortestPaths = {} 

        self.bests = []

        if not needBestLabel :
            self.bestLabel = [None, None]
            self.bestDistanceLabel = None
            self.bestDangerLabel = None
        
        fwLabelList = [] # forward labelList
        bwLabelList = [] # backward labelList
        self.directedLabelList = {
            True : fwLabelList,
            False : bwLabelList
        }




    """
    the nexts functions are unused
    """

    def addShortestPath(self, destination, totalWeight) :
        """
        shortestPaths is a dictonary with:
        Key -> the destination node
        Value -> the total weight of all arches -> then also the danger
        """
        self.shortestPaths[destination] = totalWeight

    def updatePredecessor(self, predecessor) :
        """
        Update the predecessor of the current node
        """
        self.predecessor = predecessor

    def __lt__(self, other):
        return self.index < other.index

