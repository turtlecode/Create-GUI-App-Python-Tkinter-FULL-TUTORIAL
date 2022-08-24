from tkinter import * 
from tkinter import ttk
import tkinter

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

w = Label(root, text ='Turtle Code Counter', font = "50") 
w.pack()
  
sp = Spinbox(root, from_= 0, to = 20)
sp.pack()

root.mainloop()