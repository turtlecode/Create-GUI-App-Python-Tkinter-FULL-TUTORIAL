from tkinter import * 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

w = Label(root, text ='Turtle Code', font = "50") 
w.pack()
  
frame = Frame(root)
frame.pack()
  
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
  
b1_button = Button(frame, text ="Turtle1", fg ="red")
b1_button.pack( side = LEFT)
  
b2_button = Button(frame, text ="Turtle2", fg ="brown")
b2_button.pack( side = LEFT )
  
b3_button = Button(frame, text ="Turtle3", fg ="blue")
b3_button.pack( side = LEFT )
  
b4_button = Button(bottomframe, text ="Turtle4", fg ="green")
b4_button.pack( side = BOTTOM)
  
b5_button = Button(bottomframe, text ="Turtle5", fg ="green")
b5_button.pack( side = BOTTOM)
  
b6_button = Button(bottomframe, text ="Turtle6", fg ="green")
b6_button.pack( side = BOTTOM)

root.mainloop()