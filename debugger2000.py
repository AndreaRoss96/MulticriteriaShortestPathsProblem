from PriorityQueue import PriorityQueue

def debugger(source, counter) :
    print("loop:", counter, "nodo: ", source.index, " -- neighbors: ", list(map(lambda x : x[0].index, source.neighbors)))
    for node in source.neighbors :
        if not node[0].visited :
            node[0].visited = True
            debugger(node[0], counter + 1)