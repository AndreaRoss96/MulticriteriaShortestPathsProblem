import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 21,12)
        t.pack(side="top", fill="x")

class SimpleTable(tk.Frame):

    def __init__(self, parent, rows=21, columns=12):
        stdHeight = 2
        largeHeight = 5
        smallWidth = 10
        width = 20
        column = 0

# TODO: remove v
        results = {100 : 1}
        for x in range(200, 8601, 600) : 
            results.update({x : x/1000})
        listOfResult = [results, results, results, results]
# TODO: remove ^
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="grey")
        self._widgets = []

        #first column
        smallLabel = tk.Label(self, text="Small\n<=2000", borderwidth=0, width=width, height=largeHeight)
        avgs = tk.Label(self, text="AVG", borderwidth=0, width=width, height=stdHeight, bg="light grey")
        mediumLabel = tk.Label(self, text="Medium\n2000< <=5000", borderwidth=0, width=width, height=largeHeight)
        avgm = tk.Label(self, text="AVG", borderwidth=0, width=width, height=stdHeight, bg="light grey")
        bigLabel = tk.Label(self, text="Big\n>5000", borderwidth=0, width=width, height=largeHeight)
        avgb = tk.Label(self, text="AVG", borderwidth=0, width=width, height= stdHeight, bg="light grey")
        avgLabel = tk.Label(self, text="tot", borderwidth=0, width=smallWidth, height=largeHeight)

        smallLabel.grid(row=2, column=column, sticky="nsew", padx=1, pady=1, rowspan=5)
        avgs.grid(row=7, column=column, sticky="nsew", padx=1, pady=1)
        mediumLabel.grid(row=8, column=column, sticky="nsew", padx=1, pady=1, rowspan=5)
        avgm.grid(row=13, column=column, sticky="nsew", padx=1, pady=1)
        bigLabel.grid(row=14, column=column, sticky="nsew", padx=1, pady=1, rowspan=5)
        avgb.grid(row=19, column=column, sticky="nsew", padx=1, pady=1)
        avgLabel.grid(row=20, column=column, sticky="nsew", padx=1, pady=1)

        # second column
        column = column + 1
        dkOneToAll = tk.Label(self, text="Dijkstra\none->all", borderwidth=0, width=width, height=largeHeight)
        dkOneToAll.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, rowspan=1, columnspan=2)
        self.fillColumn(listOfResult[0], column)
        
        # third column
        column = column + 2
        dkOneToOne = tk.Label(self, text="Dijkstra\none->one", borderwidth=0, width=width, height=largeHeight)
        dkOneToOne.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, rowspan=1, columnspan=2)
        self.fillColumn(listOfResult[1], column)

        # fourth column
        column = column + 2
        dkListOfCand = tk.Label(self, text="Dijkstra\nlist of candidate", borderwidth=0, width=width, height=largeHeight)
        dkListOfCand.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, rowspan=1, columnspan=2)
        self.fillColumn(listOfResult[2], column)

        # fiveth column
        column = column + 2
        aStar = tk.Label(self, text="A*", borderwidth=0, width=width, height=largeHeight)
        aStar.grid(row=0, column=column, sticky="nsew", padx=1, pady=1, rowspan=1, columnspan=2)
        self.fillColumn(listOfResult[3], column)

        # row with "weight and time" under the name of the algorithm
        for counter in range(1, column + 2, 2) :
            weightLabel = tk.Label(self, text="weight", borderwidth=0, width=smallWidth, height=stdHeight)
            timeLabel = tk.Label(self, text="time", borderwidth=0, width=smallWidth, height=stdHeight)
            weightLabel.grid(row=1, column=counter, sticky="nsew", padx=1, pady=1)
            timeLabel.grid(row=1, column=(counter + 1), sticky="nsew", padx=1, pady=1)

    def fillColumn(self, values, column) :
        aRow, bRow, cRow = 2, 8, 13
        sDist, mDist, bDist = [], [], []
        sTime, mTime, bTime = [], [], []
        
        for dist, time in values.items() :
            if dist <= 2000 :
                distLabel = tk.Label(self, text=dist, borderwidth=0)
                timeLabel = tk.Label(self, text=time, borderwidth=0)

                distLabel.grid(row = aRow, column = column, sticky="nsew", padx=1, pady=1)
                timeLabel.grid(row = aRow, column = (column + 1), sticky="nsew", padx=1, pady=1)

                sDist.append(dist)
                sTime.append(time)
                aRow += 1
            elif dist > 2000 and dist <= 5000 :
                distLabel = tk.Label(self, text=dist, borderwidth=0)
                timeLabel = tk.Label(self, text=time, borderwidth=0)

                distLabel.grid(row = bRow, column = column, sticky="nsew", padx=1, pady=1)
                timeLabel.grid(row = bRow, column = (column + 1), sticky="nsew", padx=1, pady=1)

                mDist.append(dist)
                mTime.append(time)
                bRow += 1
            else :
                distLabel = tk.Label(self, text=dist, borderwidth=0)
                timeLabel = tk.Label(self, text=time, borderwidth=0)

                distLabel.grid(row = cRow, column = column, sticky="nsew", padx=1, pady=1)
                timeLabel.grid(row = cRow, column = (column + 1), sticky="nsew", padx=1, pady=1)

                bDist.append(dist)
                bTime.append(time)
                cRow += 1
        
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

        totalDistList = [*sDist, *mDist, *bDist]
        totalTimeList = [*sTime, *mTime, *bTime]

        totalDist = tk.Label(self, text = self.avg(totalDistList), borderwidth=0)
        totalTime = tk.Label(self, text = self.avg(totalTimeList), borderwidth=0)

        totalDist.grid(row = cRow + 1, column = column, sticky="nsew", padx=1, pady=1)
        totalTime.grid(row = cRow + 1, column = column + 1, sticky="nsew", padx=1, pady=1)

    def avg(self, list) :
        return round(sum(list)/len(list), 2)


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()