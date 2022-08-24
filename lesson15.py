from tkinter import * 
from tkinter import ttk
import tkinter

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

progress = ttk.Progressbar(root, orient = HORIZONTAL,
            length = 100, mode = 'indeterminate')

def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 100
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)
    progress['value'] = 0
      
  
progress.pack(pady = 10)

Button(root, text = 'Start', command = bar).pack(pady = 10)

root.mainloop()