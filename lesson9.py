from tkinter import * 
from tkinter import ttk
import tkinter

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

name_var=tkinter.StringVar()
passw_var=tkinter.StringVar()

def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is : " + name)
    print("The password is : " + password)
     
    name_var.set("")
    passw_var.set("")

name_label = tkinter.Label(root, text = 'Username', font=('calibre',10, 'bold'))

name_entry = tkinter.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

passw_label = tkinter.Label(root, text = 'Password', font = ('calibre',10,'bold'))

passw_entry=tkinter.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

sub_btn=tkinter.Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()