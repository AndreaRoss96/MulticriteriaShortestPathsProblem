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