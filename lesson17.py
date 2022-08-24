from tkinter import * 
from tkinter import ttk
import tkinter
import tkinter.scrolledtext as st

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

ttk.Label(root, 
         text = "ScrolledText Widget Example", 
         font = ("Times New Roman", 15), 
         background = 'green', 
         foreground = "white").grid(column = 0,
                                    row = 0)

text_area = st.ScrolledText(root,
                            width = 30, 
                            height = 8, 
                            font = ("Times New Roman",
                                    15))
  
text_area.grid(column = 0, pady = 10, padx = 10)

text_area.configure(state ='normal')

root.mainloop()