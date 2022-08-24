from tkinter import * 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

v = StringVar(root, "1")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}

for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
                value = value, indicator = 0,
                background = "light blue").pack(fill = X, ipady = 5)

root.mainloop()