from tkinter import * 
from tkinter import ttk
import tkinter

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

w = Label(root, text ='Turtle Code', font = "50") 
w.pack()
    
msg = Message( root, text = "Turtle Code Youtube Channel")  
    
msg.pack() 

root.mainloop()