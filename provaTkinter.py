import tkinter as tk


def createGraph(graph, path) :

    winWidth = 500
    winHeight = 500
    r = 10 # radius of circles

    top = tk.Tk()
    can = tk.Canvas(top, width = winWidth, height = winHeight, bg = 'white')
    can.pack()
    # can.create_oval(10,10,10,10)

    for node in graph :
        if node.visited :
            can.create_oval(node.latitude-r, node.longitude-r, node.latitude+r, node.longitude+r, outline = "yellow", fill = "yellow")
            print(node.x, node.y, node.longitude, node.latitude)
        else :
            can.create_oval(node.latitude-r, node.longitude-r, node.latitude+r, node.longitude+r, outline = "black", fill = "black")
        can.pack()

    for node in path :
        if node.predecessor is not None :
            pred = node.predecessor
            can.create_line(node.latitude, node.longitude, pred.latitude, pred.longitude, fill = "red")
        can.pack()
    
    top.mainloop()
