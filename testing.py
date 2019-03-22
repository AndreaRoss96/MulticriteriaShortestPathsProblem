from node import Node

#nodes of the graph
node1 = Node(1, 10, 60)
node2 = Node(2, 20, 20)
node3 = Node(3, 40, 80)
node4 = Node(4, 40, 40)
node5 = Node(5, 60, 15)

graph = [node1,node2,node3,node4,node5]

#archs of the graph round-trip
arch1 = (node1, node2, 5)
arch2 = (node2, node1, 3)
arch3 = (node1, node3, 6)
arch4 = (node3, node1, 2)
arch5 = (node2, node4, 10)
arch6 = (node4, node2, 2)
arch7 = (node3, node4, 1)
arch8 = (node4, node3, 7)
arch9 = (node3, node5, 4)
arch10 = (node5, node3, 5)
arch11 = (node4, node5, 2)
arch12 = (node5, node4, 3)

edgeList = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8, arch9, arch10, arch11, arch12]

edgeList.sort(key = lambda elem : elem[0].index) #sorting arches for speed

#looping every edge for creaate the list of neighbors
for node in graph :
    #print("index = {0.index}\nTopOfEdgeList = {1[0][0].index}".format(node, edgeList))
    #for each arch find the destination and, if it is correct, it is added to the list of neighbor of the current node 
    while (len(edgeList) > 0) and (edgeList[0][0].index == node.index) :
        elem = edgeList.pop(0) #edgeList.pop() doesn't shift the list
        #print("the element popped:", elem[0].index, "->", elem[1].index, "w/", elem[2])
        for v in graph :
        #    print ("is next index {0.index}?" .format(v))
            if elem[1].index == v.index :
                found = True
        #        print("*yes*\nStarting node: ", node.index,"\nNode of arrival: ", v.index,"\ndistance: ", elem[2],"\n*****")
                node.neighbors.update({v : elem[2]})
                break

#print([elem.index for elem in node4.neighbors]) #the "[]"s are use to generate a list from the foreach statement

from dijkstra import dijkstraOneToAll
from dijkstra import dijkstraOneToOne
from dijkstra import dijkstraListOfCandidate
from A_Star import a_star

#print([elem.minDistance for elem in graph])

"""++++++++++++++++++++++++++++++++++++++++++++++++
************** ONE -> ALL ****************
"""
print("*"*40, "ONE TO ALL", "*"*40)
dijkstraOneToAll(graph, node1)
print("graph:", graph)
for elem, distance in node1.shortestPaths.items() :
    print("from 1 ->", elem.index, "the weight of the path is", distance)

"""+++++++++++++++++++++++++++++++++++++++++++++++++
************** ONE -> ONE ****************
"""
print("*"*40, "ONE TO ONE", "*"*40)
dijkstraOneToOne(graph, node1, node5)

pointer = node5
while pointer != node1 :
    print(pointer.index)
    pointer = pointer.predecessor


"""+++++++++++++++++++++++++++++++++++++++++++++++++
************** LIST OF CANDIDATE ****************
"""
print("*"*40, "LIST OF CANDIDATE", "*"*40)
dijkstraListOfCandidate(graph, node1, node5)

pointer = node5
while pointer != node1 :
    print(pointer.index)
    pointer = pointer.predecessor

"""+++++++++++++++++++++++++++++++++++++++++++++++++
************** A STAR ****************
"""
print("*"*40, "A STAR", "*"*40)
a_star(graph, node1, node5)

pointer = node5
while pointer != node1 :
    print(pointer.index)
    pointer = pointer.predecessor

