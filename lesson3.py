from tkinter import * 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

frame = Frame(root)                  
frame.pack()                          
  
button = Button(frame, text ='Quit Button',
                 command = root.destroy)  
button.pack()                

root.mainloop()