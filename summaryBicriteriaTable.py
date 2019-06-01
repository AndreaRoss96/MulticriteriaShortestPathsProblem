import xlsxwriter
from Node import Node
from setup import graphBuilder
import time
import pandas as pds
from utilities import initSingleNode
from labelSettingAlgorithm import labelSettingAlgorithm
from labelSettingAlgorithm import lowerBoundImprovement
from bicriteriaDijkstra import dijkstraBiCrit
from bicriteriaDijkstra import binarySearchDijkBiCr
from bicriteriaDijkstra import dijkstraBiCrIteration

dataN = pds.read_csv('graphs/paris_noeuds.csv', sep='\t', header=None)
dataA = pds.read_csv('graphs/paris_arcs.csv', sep='\t', header=None)

graph = graphBuilder(dataN.values.tolist(), dataA.values.tolist())

test = [(3176, 2586), (22474, 18289), (22066,9174)]
# [(23755, 27268), (15513, 13984), (14591, 26905), (7642, 8365), (5456, 27648),
# (27257, 23843), (6429, 6531), (234, 14318), (776, 17207), (8678, 5881),
# (15426, 2070), (26045, 16486), (3176, 2586), (22474, 18289), (22066,9174)]

workbook = xlsxwriter.Workbook('bicriteriaTable.xlsx')
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
worksheet.set_column('B:B', columnWidth)
worksheet.set_column('C:C', columnWidth)
worksheet.set_column('D:D', columnWidth)
worksheet.set_column('E:E', columnWidth)
worksheet.set_column('F:F', columnWidth)
worksheet.set_column('G:G', columnWidth + 5)
worksheet.set_column('H:H', columnWidth)


worksheet.merge_range('B1:C1', 'Dijkstra Bicriteria binary search', merge_format)
worksheet.merge_range('D1:E1', 'Label-setting algorithm', merge_format)
worksheet.merge_range('F1:H1', 'Lower bound improvement', merge_format)
worksheet.write('B2', 'Number of solution', bold)
worksheet.write('C2', 'Time (sec)', bold)
worksheet.write('D2', 'Number of solution', bold)
worksheet.write('E2', 'Time (sec)', bold)
worksheet.write('F2', 'Number of solution', bold)
worksheet.write('G2', 'Preprocessing time (sec)', bold)
worksheet.write('H2', 'Total time (sec)', bold)

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
    # initSingleNode(graph, source)
    # start = time.time()
    # infoList = binarySearchDijkBiCr(graph, source, target)
    # end = time.time()

    # worksheet.write(row, column, len(infoList))
    # column += 1
    # worksheet.write(row, column, end-start)
    # column += 1

    # ####labelSetting####
    # initSingleNode(graph, source)
    # start = time.time()
    # labelSettingAlgorithm(source, target)
    # end = time.time()

    # worksheet.write(row, column, len(target.labelList))
    # column += 1
    # worksheet.write(row, column, end-start)
    # column += 1

    # ####Preprocessing####
    # initSingleNode(graph, source)

    # startP = time.time()
    # dijkstraBiCrit(source, target, 0) # safest path => uses the target as source
    # initSingleNode(graph, source)
    # dijkstraBiCrit(source, target, 1) # shortest path => "
    # endP = time.time()

    ####LowerBound####
    initSingleNode(graph, source)
    start = time.time()
    lowerBoundImprovement(graph, source, target)
    end = time.time()

    worksheet.write(row, column, len(target.labelList))
    column += 1
    worksheet.write(row, column, end-start)
    column += 1
    worksheet.write(row, column, end-start)

worksheet.write_formula('B8', '=AVERAGE(B3:B7)')
worksheet.write_formula('C8', '=AVERAGE(C3:C7)')
worksheet.write_formula('D8', '=AVERAGE(D3:D7)')
worksheet.write_formula('E8', '=AVERAGE(E3:E7)')
worksheet.write_formula('F8', '=AVERAGE(F3:F7)')
worksheet.write_formula('G8', '=AVERAGE(G3:G7)')
worksheet.write_formula('H8', '=AVERAGE(H3:H7)')

worksheet.write_formula('B14', '=AVERAGE(B9:B13)')
worksheet.write_formula('C14', '=AVERAGE(C9:C13)')
worksheet.write_formula('D14', '=AVERAGE(D9:D13)')
worksheet.write_formula('E14', '=AVERAGE(E9:E13)')
worksheet.write_formula('F14', '=AVERAGE(F9:F13)')
worksheet.write_formula('G14', '=AVERAGE(G9:G13)')
worksheet.write_formula('H14', '=AVERAGE(H9:H13)')

worksheet.write_formula('B20', '=AVERAGE(B15:B19)')
worksheet.write_formula('C20', '=AVERAGE(C15:C19)')
worksheet.write_formula('D20', '=AVERAGE(D15:D19)')
worksheet.write_formula('E20', '=AVERAGE(E15:E19)')
worksheet.write_formula('F20', '=AVERAGE(F15:F19)')
worksheet.write_formula('G20', '=AVERAGE(G15:G19)')
worksheet.write_formula('H20', '=AVERAGE(H15:H19)')

worksheet.write_formula('B21', '=AVERAGE(B3:B7;B9:B13;B15:B19)')
worksheet.write_formula('C21', '=AVERAGE(C3:C7;C9:C13;C15:C19)')
worksheet.write_formula('D21', '=AVERAGE(D3:D7;D9:D13;D15:D19)')
worksheet.write_formula('E21', '=AVERAGE(E3:E7;E9:E13;E15:E19)')
worksheet.write_formula('F21', '=AVERAGE(F3:F7;F9:F13;F15:F19)')
worksheet.write_formula('G21', '=AVERAGE(G3:G7;G9:G13;G15:G19)')
worksheet.write_formula('H21', '=AVERAGE(H3:H7;H9:H13;H15:H19)')

workbook.close()