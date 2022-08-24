from tkinter import *

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

pane = Frame(root)
pane.pack(fill = BOTH, expand = True)

b1 = Button(pane, text = "Click me !",
            background = "red", fg = "white")
b1.pack(side = TOP, expand = True, fill = BOTH)

b2 = Button(pane, text = "Click me too",
            background = "blue", fg = "white")
b2.pack(side = TOP, expand = True, fill = BOTH)

b3 = Button(pane, text = "I'm also button",
            background = "green", fg = "white")
b3.pack(side = TOP, expand = True, fill = BOTH)
  
root.mainloop() 