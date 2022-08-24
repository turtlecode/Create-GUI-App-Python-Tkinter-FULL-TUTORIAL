from tkinter import * 
from tkinter import ttk
import tkinter

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

ttk.Label(root, text = "Combobox Example", 
          background = 'yellow', foreground ="black", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)

ttk.Label(root, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)

n = tkinter.StringVar()
monthchoosen = ttk.Combobox(root, width = 27, textvariable = n)

monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
monthchoosen.grid(column = 1, row = 5)
#monthchoosen.current()
monthchoosen.current(1)

root.mainloop()