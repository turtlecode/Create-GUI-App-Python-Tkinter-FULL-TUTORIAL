from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

def Submit():
    messagebox.askquestion("Form",
                           "Do you want to Submit")

root.geometry("100x100")

B1 = Button(root, text = "Submit", command = Submit)

B1.pack()  

root.mainloop() 