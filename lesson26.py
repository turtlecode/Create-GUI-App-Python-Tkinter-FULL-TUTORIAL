from tkinter import *
from tkinter import messagebox
# info, question, warning,
root = Tk()

root.title("Tkinter")
root.geometry("500x500")

def check():
   messagebox.askquestion("Form",
                          "Is your name correct?",
                          icon ='error')
 
root.geometry("100x100")
B1 = Button(root, text = "check", command = check)
B1.pack()
 
root.mainloop()