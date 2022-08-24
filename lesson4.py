from tkinter import * 

root = Tk()

root.title("Tkinter")
root.geometry("500x500")

user_name = Label(root,text = "Username")
user_name.place(x = 40,y = 60) 

user_password = Label(root,text = "Password")
user_password.place(x = 40,y = 100) 
   
submit_button = Button(root,text = "Submit")
submit_button.place(x = 40,y = 130)
   
user_name_input_area = Entry(root,width = 30)
user_name_input_area.place(x = 110,y = 60) 
   
user_password_entry_area = Entry(root,width = 30, show="*")
user_password_entry_area.place(x = 110,y = 100)

root.mainloop()