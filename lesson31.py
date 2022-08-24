from tkinter import * 
from tkinter import ttk

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

pw = PanedWindow(orient ='vertical')

top = ttk.Button(pw, text ="Click Me !\nI'm a Button")
top.pack(side = TOP)

pw.add(top)

bot = Checkbutton(pw, text ="Choose Me !")
bot.pack(side = TOP)

pw.add(bot)

label = Label(pw, text ="I'm a Label")
label.pack(side = TOP)
  
pw.add(label)

string = StringVar()

entry = Entry(pw, textvariable = string, font =('arial', 15, 'bold'))
entry.pack()

entry.focus_force()
  
pw.add(entry)

pw.pack(fill = BOTH, expand = True)

pw.configure(sashrelief = RAISED)
  
root.mainloop() 