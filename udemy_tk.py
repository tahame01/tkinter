import tkinter as tk
from tkinter import ttk 

root = tk.Tk()

def button1():
    print('button1')



label1 = ttk.Label(root,text='Label 1',padding=(10,20))
label1.pack(side='left',fill='y',expand=True)
button1 = ttk.Button(root,text='click me',command=button1,padding=(10,20))
button1.pack(side='top',fill='x')
button2 = ttk.Button(root,text='exit',command=root.destroy)
button2.pack(side='left',fill='y')




root.mainloop()
