
"""
Initialising all the the nodes for the dijkstra algorithm

@param graph
        the set of all nodes

@param startingNode
        the starting node
"""
def _initSingleNode(graph, source) : 
    for v in graph :
        v.reset() #reset the value of predeccor, visited and minDistance of all nodes
    source.minDistance = 0
    source.visited = True
    return graph

def dijkstraOneToAll(graph, source):
    nodeSet = [_initSingleNode (graph, source)]
    while (len(nodeSet) > 0) : 
        actualNode = min(graph, key = lambda elem : elem.ḿinDistance)
        nodeSet.remove(actualNode)
        #actualNode.visited = True
        for nextNode,distance in actualNode.neighbors :
            tmp = actualNode.minDistance + distance
            if tmp < nextNode.minDistance:
                nextNode.minDistance = tmp
                nextNode.predecessor = actualNode
                #updateNode(...)
