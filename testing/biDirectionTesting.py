import sys
import time

import pandas as pds
sys.path.append("algorithms/") # Has to be here to import the module in algorithms/
from algorithms.bidirectional.bidirectionalBicriteria import bidirectionalBicriteriaAlgorithm
from Node import Node
from setup import graphBuilder
from utilities import initSingleNode
from graphPlotter import bidirectionPlotGraph

dataN = pds.read_csv('graphs/cesena/cesena_nodes.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/cesena/cesena_arcs_bidir.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

source = graph[5221]#23755]#2000]#
target = graph[72]#27268]#2689]# #5142 or 2886


print("\n", "*"*40, "bidirection ALGORITHM", "*"*40)
initSingleNode(graph, source)

tmp_list= []
for n in range (0, 1): # increase the second value to make an average
    initSingleNode(graph, source)
    start = time.time()
    paretoList = bidirectionalBicriteriaAlgorithm(source, target) # algorithm
    end = time.time()
    tmp_list.append(end-start)
print("AVGtime:", sum(tmp_list) / len(tmp_list))
print(len(paretoList[0]))

########################
##### BACKTRACKING #####
########################
"""
paretoLabel = (dist, dang, owner, (fwPred, fwOwnerListPost, fwpredListPos), (bwPred, bwOwnerListPost, bwpredListPos))
"""
# for elem in paretoList[0] :
#     print(elem[0], elem[1])

ownerSet = set()
for paretoLabel in paretoList[0] :
    ownerSet.add(paretoLabel[2])

toPrint = []
graphList = []
for owner in ownerSet :
    # print("owner:", owner.index)
    tmpPrintFw = []
    graphFw = []
    for label in owner.directedLabelList[True] :
        printListFw = [label[2].index]
        nodeList = [label[2]]
        while label[3] != None :
            node = label[3]
            nodeList.append(node)
            lenList = len(node.directedLabelList[True])
            index = label[5] if label[5] < lenList else lenList - 1
            label = node.directedLabelList[True][index]
            printListFw.append(node.index)
        graphFw.append(nodeList)
        # print(*printListFw, sep="<-")
        tmpPrintFw.append(printListFw)
    # print("FINITO FW")
    tmpPrintBw = []
    graphBw = []
    for label in owner.directedLabelList[False] :
        printListBw = []
        nodeList = [label[2]]
        while label[3] != None :
            node = label[3]
            nodeList.append(node)
            lenList = len(node.directedLabelList[False])
            index = label[5] if label[5] < lenList else lenList - 1
            label = node.directedLabelList[False][index]
            printListBw.append(node.index)
        graphBw.append(nodeList)
        # print(*printListBw, sep="->")
        tmpPrintBw.append(printListBw)
    # print("FINITO BW")
    for fwElem in tmpPrintFw :
        for bwElem in tmpPrintBw :
            fwElem.reverse()
            toPrint.append(fwElem + bwElem)
            fwElem.reverse()

    for fw in graphFw : 
        for bw in graphBw :
            fw.reverse()
            graphList.append(fw + bw)
            fw.reverse()

        

printSet = set(tuple(i) for i in toPrint)
# for elem in printSet :
#     print(*elem, sep='->')

graphSet = set(tuple(i) for i in graphList)
bidirectionPlotGraph(graph, graphSet, source, target)

    # print("ParetoLabel:", paretoLabel)
    # print(paretoLabel[2].directedLabelList[True])
    # print("owner:", paretoLabel[2].index)
    # fwLabel = paretoLabel[3][0]
    # for label in fwLabel.directedLabelList[True] :
    #     printListFw = []
    #     nodeList = [label[2]]
    #     while label[3] != None :
    #         node = label[3]
    #         nodeList.append(node)
    #         lenList = len(node.directedLabelList[True])
    #         index = label[5] if label[5] < lenList else lenList - 1
    #         label = node.directedLabelList[True][index]
    #         printListFw.append(node.index)
    #     print(*printListFw, sep="<-")
    # print("FINITO FW")
    # bwLabel = paretoLabel[4][0]
    # for label in bwLabel.directedLabelList[False] :
    #     printListBw = []
    #     nodeList = [label[2]]
    #     while label[3] != None :
    #         node = label[3]
    #         nodeList.append(node)
    #         lenList = len(node.directedLabelList[False])
    #         index = label[5] if label[5] < lenList else lenList - 1
    #         label = node.directedLabelList[False][index]
    #         printListBw.append(node.index)
    #     print(*printListBw, sep="<-")
    # print("FINITO BW")

    

    # for fwLabel in paretoLabel[2].directedLabelList[True] :
    #     printListFw = []
    #     while fwLabel[3] != None :
    #         node = fwLabel[3]
            
    #         lenList = len(node.labelList)
    #         index = fwLabel[5] if fwLabel[5] < lenList else lenList - 1
    #         fwLabel = node.directedLabelList[True][index]
    #         printListFw.append(node.index)

    #         for bwLabel in target.labelList :
    #             printListBw = []
    #             while bwLabel[3] != paretoLabel[2] : # as long the predecessor is != from the owner of the pareto label
    #                 node = bwLabel[3]
                    
    #                 lenList = len(node.labelList)
    #                 index = bwLabel[5] if bwLabel[5] < lenList else lenList - 1
    #                 bwLabel = node.directedLabelList[False][index]
    #                 printListBw.append(node.index)
    #             print(*printListFw, *printListBw, sep="<-") 



