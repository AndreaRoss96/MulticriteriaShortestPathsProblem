import tkinter as tk

class SummaryTable(tk.Tk):
            
    def __init__(self, listOfResult):
        tk.Tk.__init__(self)
        t = SimpleTable(self, listOfResult)
        t.pack(side="top", fill="x")

class SimpleTable(tk.Frame):

    def __init__(self, parent, listOfResult):
        global stdBgColor
        stdBgColor = "white"

        stdHeight = 1
        largeHeight = 2
        smallWidth = 7
        mediumWidth = 11
        width = 15
        column = 0

        rowSpan = 5
        colSpan = 2

        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="grey")
        self._widgets = []

        listOfResult = dict(sorted(listOfResult.items(), key= lambda x : x[1])) #sorting the dictonary in base of the weight

        #first column
        smallLabel = tk.Label(self, text="Small\n<=2000", borderwidth=0, width=width, height=largeHeight, bg=stdBgColor)
        avgs = tk.Label(self, text="AVG", borderwidth=0, width=width, height=stdHeight, bg="light grey")
        mediumLabel = tk.Label(self, text="Medium\n2000< <=5000", borderwidth=0, width=width, height=largeHeight, bg=stdBgColor)
        avgm = tk.Label(self, text="AVG", borderwidth=0, width=width, height=stdHeight, bg="light grey")
        bigLabel = tk.Label(self, text="Big\n>5000", borderwidth=0, width=width, height=largeHeight, bg=stdBgColor)
        avgb = tk.Label(self, text="AVG", borderwidth=0, width=width, height= stdHeight, bg="light grey")
        avgLabel = tk.Label(self, text="tot", borderwidth=0, width=smallWidth, height=largeHeight, bg=stdBgColor)

        smallRow, mediumRow, bigRow = 2, 8, 14
        smallLabel.grid(row=smallRow, column=column, sticky="nsew", padx=1, pady=1, rowspan=rowSpan)
        avgs.grid(row=mediumRow - 1, column=column, sticky="nsew", padx=1, pady=1, columnspan = colSpan)
        mediumLabel.grid(row=mediumRow, column=column, sticky="nsew", padx=1, pady=1, rowspan=rowSpan)
        avgm.grid(row=bigRow - 1, column=column, sticky="nsew", padx=1, pady=1, columnspan = colSpan)
        bigLabel.grid(row=bigRow, column=column, sticky="nsew", padx=1, pady=1, rowspan=rowSpan)
        avgb.grid(row=bigRow + 5, column=column, sticky="nsew", padx=1, pady=1, columnspan = colSpan)
        avgLabel.grid(row=bigRow + 6, column=column, sticky="nsew", padx=1, pady=1, columnspan = colSpan)

        
        #column dedicated to the nodes source -> target
        column = column + 1
        valueList = {"oneToAll" : [], "oneToOne" : [], "ListOfCand" : [], "aStar" : []}
        for indx, nodes in enumerate(listOfResult.keys()) :
            nodeLabel = tk.Label(self, text="{0}->{1}".format(nodes[0], nodes[1]), borderwidth=0, width=mediumWidth, height=largeHeight, bg=stdBgColor)
            if indx < 5 :
                nodeLabel.grid(row=smallRow, column=column, sticky="nsew", padx=1, pady=1)
                smallRow = smallRow + 1
            elif indx >= 5 and indx <= 9 :
                nodeLabel.grid(row=mediumRow, column=column, sticky="nsew", padx=1, pady=1)
                mediumRow = mediumRow + 1
            else :
                nodeLabel.grid(row=bigRow, column=column, sticky="nsew", padx=1, pady=1)
                bigRow = bigRow + 1
            elem = listOfResult.get(nodes)
            valueList.get("oneToAll").append(elem[0])
            valueList.get("oneToOne").append(elem[1])
            valueList.get("ListOfCand").append(elem[2])
            valueList.get("aStar").append(elem[3])


        # oneToAll column
        column = column + 1
        dkOneToAll = tk.Label(self, text="Dijkstra\none->all", borderwidth=0, width=width, height=largeHeight, bg=stdBgColor)
        dkOneToAll.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, rowspan=1, columnspan=2)
        self.fillColumn(valueList.get("oneToAll"), column)
        
        # OneToOne column
        column = column + 2
        dkOneToOne = tk.Label(self, text="Dijkstra\none->one", borderwidth=0, width=width, height=largeHeight, bg=stdBgColor)
        dkOneToOne.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, columnspan=2)
        self.fillColumn(valueList.get("oneToOne"), column)

        # LoC column
        column = column + 2
        dkListOfCand = tk.Label(self, text="Dijkstra\nlist of candidate", borderwidth=0, width=width, height=largeHeight, bg=stdBgColor)
        dkListOfCand.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, columnspan=2)
        self.fillColumn(valueList.get("ListOfCand"), column)

        # A* column
        column = column + 2
        aStar = tk.Label(self, text="A*", borderwidth=0, width=width, height=largeHeight, bg=stdBgColor)
        aStar.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, columnspan=2)
        self.fillColumn(valueList.get("aStar"), column)

        # row with "weight and time" under the name of the algorithm
        for counter in range(1, column, 2) :
            weightLabel = tk.Label(self, text="weight", borderwidth=0, width=smallWidth, height=stdHeight, bg=stdBgColor)
            timeLabel = tk.Label(self, text="time (sec)", borderwidth=0, width=smallWidth, height=stdHeight, bg=stdBgColor)
            weightLabel.grid(row=1, column=counter + 1, sticky="nsew", padx=1, pady=1)
            timeLabel.grid(row=1, column=(counter + 2), sticky="nsew", padx=1, pady=1)

    def fillColumn(self, valuesList, column) :
        """
        Fill the selected column with the value of weight and time passed by input
        """

        aRow, bRow, cRow = 2, 8, 14
        sDist, mDist, bDist = [], [], [] # Those list are used for calculating the average weigth of each group (small, medium, big)
        sTime, mTime, bTime = [], [], [] # like above but fot the time
        
        for dist, time in valuesList :
            if dist <= 2000 :
                distLabel = tk.Label(self, text=dist, borderwidth=0, bg=stdBgColor)
                timeLabel = tk.Label(self, text=time, borderwidth=0, bg=stdBgColor)

                distLabel.grid(row = aRow, column = column, sticky="nsew", padx=1, pady=1)
                timeLabel.grid(row = aRow, column = (column + 1), sticky="nsew", padx=1, pady=1)

                sDist.append(dist)
                sTime.append(time)
                aRow += 1
            elif dist > 2000 and dist <= 5000 :
                distLabel = tk.Label(self, text=dist, borderwidth=0, bg=stdBgColor)
                timeLabel = tk.Label(self, text=time, borderwidth=0, bg=stdBgColor)

                distLabel.grid(row = bRow, column = column, sticky="nsew", padx=1, pady=1)
                timeLabel.grid(row = bRow, column = (column + 1), sticky="nsew", padx=1, pady=1)

                mDist.append(dist)
                mTime.append(time)
                bRow += 1
            else :
                distLabel = tk.Label(self, text=dist, borderwidth=0, bg=stdBgColor)
                timeLabel = tk.Label(self, text=time, borderwidth=0, bg=stdBgColor)

                distLabel.grid(row = cRow, column = column, sticky="nsew", padx=1, pady=1)
                timeLabel.grid(row = cRow, column = (column + 1), sticky="nsew", padx=1, pady=1)

                bDist.append(dist)
                bTime.append(time)
                cRow += 1
        
        # labels for the averages values
        avgsdLabel = tk.Label(self, text = self.avg(sDist), borderwidth=0, bg="light grey")
        avgmdLabel = tk.Label(self, text = self.avg(mDist), borderwidth=0, bg="light grey")
        avgbdLabel = tk.Label(self, text = self.avg(bDist), borderwidth=0, bg="light grey")
        avgstLabel = tk.Label(self, text = self.avg(sTime), borderwidth=0, bg="light grey")
        avgmtLabel = tk.Label(self, text = self.avg(mTime), borderwidth=0, bg="light grey")
        avgbtLabel = tk.Label(self, text = self.avg(bTime), borderwidth=0, bg="light grey")

        avgsdLabel.grid(row = aRow, column = column, sticky="nsew", padx=1, pady=1)
        avgmdLabel.grid(row = bRow, column = column, sticky="nsew", padx=1, pady=1)
        avgbdLabel.grid(row = cRow, column = column, sticky="nsew", padx=1, pady=1)
        avgstLabel.grid(row = aRow, column = (column + 1), sticky="nsew", padx=1, pady=1)
        avgmtLabel.grid(row = bRow, column = (column + 1), sticky="nsew", padx=1, pady=1)
        avgbtLabel.grid(row = cRow, column = (column + 1), sticky="nsew", padx=1, pady=1)

        # total average of all values, so without considering small, medium and big
        totalDistList = [*sDist, *mDist, *bDist]
        totalTimeList = [*sTime, *mTime, *bTime]

        totalDist = tk.Label(self, text = self.avg(totalDistList), borderwidth=0, bg=stdBgColor)
        totalTime = tk.Label(self, text = self.avg(totalTimeList), borderwidth=0, bg=stdBgColor)

        totalDist.grid(row = cRow + 1, column = column, sticky="nsew", padx=1, pady=1)
        totalTime.grid(row = cRow + 1, column = column + 1, sticky="nsew", padx=1, pady=1)

    def avg(self, list) :
        """
        Calculate the average value of a list
        """
        return sum(list)/len(list)