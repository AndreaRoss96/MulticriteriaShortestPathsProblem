from setup import graphBuilder
from dijkstra import dijkstraOneToAll
from dijkstra import dijkstraOneToOne
from dijkstra import dijkstraListOfCandidate
from a_star import a_star
from utilities import initSingleNode
import pandas as pds
import time
import random
import sys
from summaryTable import SummaryTable

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

def valuesCalculator(graph, source, target) :
    resList = []

    initSingleNode(graph, source)
    start = time.time()
    dijkstraOneToAll(source)             #one to all
    end = time.time()
    dist = source.shortestPaths.get(target)
    times = end - start    
    resList.append((dist, times))

    initSingleNode(graph, source)
    start = time.time()
    dijkstraOneToOne(graph, source, target)     #one to one
    end = time.time()
    dist = target.minWeight 
    times = end - start
    resList.append((dist, times))
    
    initSingleNode(graph, source)
    start = time.time()
    dijkstraListOfCandidate(source, target) #list of candiadate
    end = time.time()
    dist = target.minWeight
    times = end - start
    resList.append((dist, times))

    initSingleNode(graph, source)
    start = time.time()
    a_star(source, target)                #a star
    end = time.time()
    dist = target.minWeight
    times = end - start
    resList.append((dist, times))

    return resList

"""
I have to test at least 15 different couple of nodes, to obtain all the searched solution
in the summary table
"""
condition = True
listSmall = {}
listMedium = {}
listBig = {}
while condition :
    start = end = 0
    source = graph[random.randint(0, 29085)]
    target = graph[random.randint(0, 29085)]

    initSingleNode(graph, source)
    dijkstraListOfCandidate(source, target)
    dist = target.minWeight

    if not (0 < dist < sys.maxsize) :
        print("continue")
        continue

    print("good loop")

    if dist <= 2000 :
        if len(listSmall) < 5 :
            print("list small:", dist)
            values = valuesCalculator(graph, source, target)
            listSmall.update({(source.index, target.index) : values})
    elif 2000 < dist <= 5000 :
        if len(listMedium) < 5 :
            print("list medium:", dist)
            values = valuesCalculator(graph, source, target)
            listMedium.update({(source.index, target.index) : values})
    else :
        if len(listBig) < 5 :
            print("list big:", dist)
            values = valuesCalculator(graph, source, target)
            listBig.update({(source.index, target.index) : values})
    
    if len(listSmall) == 5 and len(listMedium) == 5 and len(listBig) == 5 :
        condition = not condition
        summary = {**listSmall, **listMedium, **listBig}

print(summary)
app = SummaryTable(summary)
app.mainloop()
