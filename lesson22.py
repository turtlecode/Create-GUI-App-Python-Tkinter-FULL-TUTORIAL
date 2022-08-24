from tkinter import * 
from tkinter import ttk 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

treev = ttk.Treeview(root, selectmode ='browse')
treev.pack(side ='top')

verscrlbar = ttk.Scrollbar(root,
                           orient ="vertical",
                           command = treev.yview)

verscrlbar.pack(side ='right', fill ='x')

treev.configure(xscrollcommand = verscrlbar.set)

treev["columns"] = ("1", "2", "3")

treev['show'] = 'headings'

treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')

treev.heading("1", text ="Name")
treev.heading("2", text ="Sex")
treev.heading("3", text ="Age")

treev.insert("", 'end', text ="L1",
             values =("Nidhi", "F", "25"))
treev.insert("", 'end', text ="L2",
             values =("Nisha", "F", "23"))
treev.insert("", 'end', text ="L3",
             values =("Preeti", "F", "27"))
treev.insert("", 'end', text ="L4",
             values =("Rahul", "M", "20"))
treev.insert("", 'end', text ="L5",
             values =("Sonu", "F", "18"))
treev.insert("", 'end', text ="L6",
             values =("Rohit", "M", "19"))
treev.insert("", 'end', text ="L7",
             values =("Geeta", "F", "25"))
treev.insert("", 'end', text ="L8",
             values =("Ankit", "M", "22"))
treev.insert("", 'end', text ="L10",
             values =("Mukul", "F", "25"))
treev.insert("", 'end', text ="L11",
             values =("Mohit", "M", "16"))
treev.insert("", 'end', text ="L12",
             values =("Vivek", "M", "22"))
treev.insert("", 'end', text ="L13",
             values =("Suman", "F", "30"))

root.mainloop()