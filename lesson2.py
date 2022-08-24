'''
from tkinter import * 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

frame = Frame(root)                  
frame.pack()                          
  
button = Button(frame, text ='Turtle Button')  
button.pack()                

root.mainloop()


'''
from tkinter import * 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

def click():
  print('Button Clicked')

frame = Frame(root)                  
frame.pack()                          
  
button = Button(frame, text ='Turtle Button', command = click)  
button.pack()                

root.mainloop()