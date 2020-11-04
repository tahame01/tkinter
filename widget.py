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

image = Image.open('hack.jpg').resize((50,50))
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root,image=photo,padding=10,textvariable=textVar,compound='right')
textVar.set('hello paikhana')

# Remember that if you pack early u can't use further commands
text = tk.Text(root,height=8)
text.pack()
text.focus()

label.pack()

button =ttk.Button(root,text='submit').pack()




root.mainloop()