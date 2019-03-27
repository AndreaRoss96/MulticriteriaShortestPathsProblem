from node import Node
"""
In this file are present the function that will be used
for the setup of the program
"""

def graphBuilder(nodes, arches):
    """
    This method will return the graph with all arches and all nodes ready to be examinated

    nodes : list of nodes [index, lat, long]
    arches : list of arches [startingNode, endingNode, weight]
    """
    graph = []
    for node in nodes :
        graph.append(Node(*node))

    arches.sort(key = lambda arch : arch[0])  # sorting arches by ascending starting node's index -> speed up the creation of the graph

    # binding of arches to the nodes
    for node in graph :
        # when the first element of the arch list is the same of the actual node, it will move to the next node
        while len(arches) > 0 and arches[0][0] == node.index :
            arch = arches.pop(0)     # .pop() doesn't shift the list
            for endingNode in graph :
                if arch[1] == endingNode.index :
                    # when the ending node is found, it will update the neighbors list of the starting node, using the last arch
                    node.neighbors.update({endingNode : arch[2]})
                    break

    return graph