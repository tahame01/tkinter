import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root = tk.Tk()


textVar = tk.StringVar()

image = Image.open('hack.jpg').resize((500,500))
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root,image=photo,padding=10,textvariable=textVar,compound='right')
textVar.set('hello paikhana')

label.pack()

button =ttk.Button(root,text='submit').pack()




root.mainloop()