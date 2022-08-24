from tkinter import *

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

l1 = Label(root, text = "First:")
l2 = Label(root, text = "Second:")

l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
  
root.mainloop() 