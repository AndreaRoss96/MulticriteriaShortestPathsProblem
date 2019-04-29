import heapq

# took from https://www.redblobgames.com/pathfinding/a-star/implementation.html

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
        """
        simlar to heappush(thisQueue, (2, "example"))
                  heappush(thisQueue, (1, "example"))
                  heappop(thisQueue) >> (1, "example")
        """
    
    def getMin(self):
        return heapq.heappop(self.elements)[1]

    def print(self):
        print(self.elements)
        for elem in self.elements :
            print("element:", elem[1].index)

    def containsNode(self, node) :
        nodeList = list(map(lambda x : x[1], self.elements))
        return node in nodeList
