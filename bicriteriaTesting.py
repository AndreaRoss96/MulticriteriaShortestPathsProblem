from node import Node
from setup import graphBuilder
import time
import pandas as pds

from utilities import initSingleNode
from labelSettingAlgorithm import labelSettingAlgorithm
from bicriteriaDijkstra import dijkstraBiCrit

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)


graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())
source = graph[2000]
target = graph[2689]

print("*"*40, "BICRITERIA DIJKSTRA", "*"*40)
"""
here are implemente a sort of binary search to get some solution, the classic way (testing.py)
is more precisely (generally find more solution), but slowlest
"""
start = time.time()

leftList = [] # i risultati alpha = 0
rightList = [] # i risultati alpha = 1

totList = [] # [(distDang, alpha), ...]

high = 1
low = 0

initSingleNode(graph, source)
dijkstraBiCrit(source, target, high)
res = (target.distance, target.danger)
rightList.append(res)
totList.append((res, high))

initSingleNode(graph, source)
dijkstraBiCrit(source, target, low)
res = (target.distance, target.danger)
leftList.append(res)
totList.append((res, low))

precision = 2
exe = 0
counter = 0
approx = 4
while exe <= precision :
    counter += 1
    alpha = (high - low) / 2
    tmp = str(alpha) # taking the first two decimal number  27891s
    alpha = float(tmp[:approx])
    if alpha > 0 :
        alpha = alpha + low
        initSingleNode(graph, source)
        dijkstraBiCrit(source, target, alpha)
        res = (target.distance, target.danger)

        if res in leftList :
            low = alpha
        elif res in rightList :
            high = alpha
        else :
            if res[0] < leftList[len(leftList) - 1][0] : # res è più piccolo del più piccolo valore di left?
                leftList.append(res)
                totList.append((res, alpha))
                high = alpha
            # elif res[0] > rightList[len(rightList) - 1][0] : # res è più grande del più grande volre di right?
            else:
                rightList.append(res)
                totList.append((res, alpha))
                low = alpha
    else :
        exe += 1
        high = 1
        low = 0

leftList.extend(rightList)
end = time.time()
print(totList)
print("time: ", end - start)
print("loops:", counter)



print("*"*40, "LABEL SETTING ALGORITHM", "*"*40)
initSingleNode(graph, source)

start = time.time()
labelSettingAlgorithm(source, target)
end = time.time()

print("time:", end-start)
print("all path to target", target.index, ":")
for label in target.labelList :
    print("dist:", label[0], "\ndang:", label[1], "\npredecessor:",label[3].index, "\n============")

# label = target.labelList[0]
#########################
# BACKTRACKING V
# while label[3] != None :
#     index = label[4]
#     node = label[3]
#     label = node.labelList[index]
#     print(label[2].index)


