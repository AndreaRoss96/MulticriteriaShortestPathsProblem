import pandas as pd
from random import uniform, randint, shuffle

fileNode = "graphs/5thousand2Nodes.csv"
fileArches = "graphs/5thousand2Arches.csv"
nodeNumber = 5000
arcsPerNodes = 2

nodeList = []
arcList = []

for i in range(0, nodeNumber+1) :
    x, y = uniform(-180,180), uniform(-90, 90)
    nodeList.append([i, x, y])

# shuffle(nodeList)

for a in range(1, arcsPerNodes+1):
    print(a)
    for i in range(0, nodeNumber+1) :
        randOne = randint(1, 801)
        randTwo = randint(1, 801)
        endingNode = i+a
        if endingNode >= len(nodeList) :
            endingNode = endingNode%(len(nodeList))
        arcGoing = [nodeList[i][0], nodeList[endingNode][0], randOne, randTwo]
        arcReturn = [nodeList[endingNode][0], nodeList[i][0], randOne, randTwo]
        arcList.extend([arcGoing, arcReturn])

nodeList.sort(key = lambda node : node[0])
dfn = pd.DataFrame(nodeList)
dfa = pd.DataFrame(arcList)
dfn.to_csv(fileNode, sep='\t', header=False, index=False)
dfa.to_csv(fileArches, sep='\t', header=False, index=False)
