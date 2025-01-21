'''import tkinter as tk

def onclick():
    txt=el.get()
    print("\n")
    print(txt,"%s" %(txt))
root=tk.Tk()
root.geometry("250x400")
root.title("Button Creation")
e1=tk.Entry(root,font=("arial",15,'bold'),width=16,bd=4,bg='blue')
e1.place(x=25,y=20)
b1=tk.Button(root,padx=16,pady=10,bd=4,bg='green',text='clock',font=('arial',12,'bold'),command=onclick)
b1.place(x=65,y=60)
tk.mainloop()'''

'''import tkinter as tk
root=tk.Tk()
root.geometry("250x400")
root.title("Button Creation")
e1=tk.Entry(root,font=("arial",15,'bold'),width=16,bd=4,bg='blue')
e1.place(x=25,y=20)
b1=tk.Button(root,padx=16,pady=10,bd=4,bg='green',text='clock',font=('arial',12,'bold'),command=onclick)
b1.place(x=65,y=60)
tk.mainloop()'''



# !/usr/bin/python3  
from tkinter import *  
top = Tk()  
top.geometry("400x250")  
name = Label(top, text = "Name").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30, y = 90)  
password = Label(top, text = "Password").place(x = 30, y = 130)  
e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 95, y = 130)  
top.mainloop()  
