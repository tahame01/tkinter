import tkinter as tk
from tkinter import ttk



win = tk.Tk()
win.title('test window')


def clicked():
    label1.configure(text='i am clicked',background='green')
    button1.configure(text='yellow')



label1 = ttk.Label(win,text='i will change')
label1.grid(row=0,column=0)


#ttk button don't have background property
button1 = ttk.Button(win,text='submit',command=clicked)
button1.grid(row=1,column=0)

button2 = ttk.Button(win,text='close',command=win.destroy)
button2.grid(row=1,column=1)






win.mainloop()