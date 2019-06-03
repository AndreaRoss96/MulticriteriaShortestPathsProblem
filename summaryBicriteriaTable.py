import sys
import time

sys.path.append("algorithms/")

import pandas as pds
import xlsxwriter as xls 
from algorithms.bicriteriaDijkstra import (binarySearchDijkBiCr, dijkstraBiCrit,
                                dijkstraBiCrIteration)
from algorithms.labelSettingAlgorithm import labelSettingAlgorithm, lowerBoundImprovement
from Node import Node
from setup import graphBuilder
from utilities import initSingleNode



dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

test = [(23755, 27268), (15513, 13984), (14591, 26905), (7642, 8365), (5456, 27648),
(27257, 23843), (6429, 6531), (234, 14318), (776, 17207), (8678, 5881),
(15426, 2070), (26045, 16486), (3176, 2586), (22474, 18289), (22066,9174)]

workbook = xls.Workbook('bicriteriaTable.xlsx')
worksheet = workbook.add_worksheet()
merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'bg_color': 'Gray'})
bold = workbook.add_format({'bold': True})
columnWidth = 20
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', columnWidth - 5)
worksheet.set_column('C:C', columnWidth)
worksheet.set_column('D:D', columnWidth - 5)
worksheet.set_column('E:E', columnWidth)
worksheet.set_column('F:F', columnWidth - 5)
worksheet.set_column('G:G', columnWidth + 5)
worksheet.set_column('H:H', columnWidth)


worksheet.merge_range('B1:C1', 'Dijkstra Bicriteria binary search', merge_format)
worksheet.merge_range('D1:F1', 'Label-setting algorithm', merge_format)
worksheet.merge_range('G1:J1', 'Lower bound improvement', merge_format)
worksheet.write('A2', 'Source->target', bold)
worksheet.write('B2', 'N° solution', bold)
worksheet.write('C2', 'Time (sec)', bold)
worksheet.write('D2', 'N° solution', bold)
worksheet.write('E2', 'Time (sec)', bold)
worksheet.write('F2', 'Loops', bold)
worksheet.write('G2', 'N° solution', bold)
worksheet.write('H2', 'Preprocessing time (sec)', bold)
worksheet.write('I2', 'Total time (sec)', bold)
worksheet.write('J2', 'Loops', bold)

const = 0

for row, nodes in enumerate(test) :
    column = 1
    row = row + 2 + const
    if row == 6 :
        const = 1
    elif row == 12 :
        const = 2

    
    message = str(nodes[0]) + "->" + str(nodes[1])
    worksheet.write(row, 0, message)
    
    source = graph[nodes[0]]
    target = graph[nodes[1]]

    ####Binary search#####
    initSingleNode(graph, source)
    start = time.time()
    infoList = binarySearchDijkBiCr(graph, source, target)
    end = time.time()

    worksheet.write(row, column, len(infoList))
    column += 1
    worksheet.write(row, column, end-start)
    column += 1

    ####labelSetting####
    initSingleNode(graph, source)
    start = time.time()
    loop = labelSettingAlgorithm(source, target)
    end = time.time()

    worksheet.write(row, column, len(target.labelList))
    column += 1
    worksheet.write(row, column, end-start)
    column += 1
    worksheet.write(row, column, loop)
    column += 1

    ####Preprocessing####
    initSingleNode(graph, source)

    startP = time.time()
    visitedNodes = dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
    initSingleNode(visitedNodes, source)
    dijkstraBiCrit(source, target, 1) # shortest path => "
    endP = time.time()

    ####LowerBound####
    initSingleNode(graph, source)
    for v in graph: #reinitialize nodes for lowerboundImp
        v.resetValue(False)  # reset the value of predecessor, visited and minWeight of all nodes
    source.minWeight = 0
    source.visited = True

    start = time.time()
    loop = lowerBoundImprovement(graph, source, target)
    end = time.time()

    worksheet.write(row, column, len(target.labelList))
    column += 1
    worksheet.write(row, column, endP-startP)
    column += 1
    worksheet.write(row, column, end-start)
    column += 1
    worksheet.write(row, column, loop)
    

worksheet.write_formula('B8', '=AVERAGE(B3:B7)', bold)
worksheet.write_formula('C8', '=AVERAGE(C3:C7)', bold)
worksheet.write_formula('D8', '=AVERAGE(D3:D7)', bold)
worksheet.write_formula('E8', '=AVERAGE(E3:E7)', bold)
worksheet.write_formula('F8', '=AVERAGE(F3:F7)', bold)
worksheet.write_formula('G8', '=AVERAGE(G3:G7)', bold)
worksheet.write_formula('H8', '=AVERAGE(H3:H7)', bold)
worksheet.write_formula('I8', '=AVERAGE(I3:I7)', bold)
worksheet.write_formula('J8', '=AVERAGE(J3:J7)', bold)

worksheet.write_formula('B14', '=AVERAGE(B9:B13)', bold)
worksheet.write_formula('C14', '=AVERAGE(C9:C13)', bold)
worksheet.write_formula('D14', '=AVERAGE(D9:D13)', bold)
worksheet.write_formula('E14', '=AVERAGE(E9:E13)', bold)
worksheet.write_formula('F14', '=AVERAGE(F9:F13)', bold)
worksheet.write_formula('G14', '=AVERAGE(G9:G13)', bold)
worksheet.write_formula('H14', '=AVERAGE(H9:H13)', bold)
worksheet.write_formula('I14', '=AVERAGE(I9:I13)', bold)
worksheet.write_formula('J14', '=AVERAGE(J9:J13)', bold)

worksheet.write_formula('B20', '=AVERAGE(B15:B19)', bold)
worksheet.write_formula('C20', '=AVERAGE(C15:C19)', bold)
worksheet.write_formula('D20', '=AVERAGE(D15:D19)', bold)
worksheet.write_formula('E20', '=AVERAGE(E15:E19)', bold)
worksheet.write_formula('F20', '=AVERAGE(F15:F19)', bold)
worksheet.write_formula('G20', '=AVERAGE(G15:G19)', bold)
worksheet.write_formula('H20', '=AVERAGE(H15:H19)', bold)
worksheet.write_formula('I20', '=AVERAGE(I15:I19)', bold)
worksheet.write_formula('J20', '=AVERAGE(J15:J19)', bold)

worksheet.write_formula('B21', '=AVERAGE(B3:B7;B9:B13;B15:B19)', bold)
worksheet.write_formula('C21', '=AVERAGE(C3:C7;C9:C13;C15:C19)', bold)
worksheet.write_formula('D21', '=AVERAGE(D3:D7;D9:D13;D15:D19)', bold)
worksheet.write_formula('E21', '=AVERAGE(E3:E7;E9:E13;E15:E19)', bold)
worksheet.write_formula('F21', '=AVERAGE(F3:F7;F9:F13;F15:F19)', bold)
worksheet.write_formula('G21', '=AVERAGE(G3:G7;G9:G13;G15:G19)', bold)
worksheet.write_formula('H21', '=AVERAGE(H3:H7;H9:H13;H15:H19)', bold)
worksheet.write_formula('I21', '=AVERAGE(I3:I7;I9:I13;I15:I19)', bold)
worksheet.write_formula('J21', '=AVERAGE(J3:J7;J9:J13;J15:J19)', bold)

workbook.close()
