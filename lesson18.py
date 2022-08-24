from tkinter import * 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

listbox = Listbox(root, height = 10, 
                  width = 15, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")

label = Label(root, text = " FOOD ITEMS") 

listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

label.pack()
listbox.pack()

root.mainloop()