from tkinter import * 
from tkinter import ttk 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

label1 = Label(root, text = "This is the root window")

def open_Toplevel2(): 

    top2 = Toplevel()

    top2.title("Toplevel2")

    top2.geometry("200x100")

    label = Label(top2,
                  text = "This is a Toplevel2 window")

    button = Button(top2, text = "Exit",
                    command = top2.destroy)
     
    label.pack()
    button.pack()

    top2.mainloop()

def open_Toplevel1(): 
    top1 = Toplevel(root)

    top1.title("Toplevel1")

    top1.geometry("200x200")

    label = Label(top1,
                  text = "This is a Toplevel1 window")

    button1 = Button(top1, text = "Exit",
                     command = top1.destroy)

    button2 = Button(top1, text = "open toplevel2",
                     command = open_Toplevel2)
     
    label.pack()
    button2.pack()
    button1.pack()
    top1.mainloop()

button = Button(root, text = "open toplevel1",
                command = open_Toplevel1)
label1.pack()

button.place(x = 155, y = 50)

root.mainloop()