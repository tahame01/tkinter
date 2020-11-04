import tkinter as tk
from tkinter import ttk



win = tk.Tk()
win.title('test window')

name = tk.StringVar()


def clicked():
    label1.configure(text='Hello '+ name.get(),background='yellow')
    button1.configure(state='disabled')
    button1.configure(text='cant click me now')


label1 = ttk.Label(win,text='Please input your name please ')
label1.grid(row=0,column=0)

text_entry = ttk.Entry(win,width=12,textvariable=name)
text_entry.grid(row=1,column=0)
text_entry.focus()

#ttk button don't have background property
button1 = ttk.Button(win,text='submit',command=clicked)
button1.grid(row=2,column=0)

combo_box = ttk.Combobox(text='select a number:',values=(1,2,3,4))
combo_box.grid(row=3,column=0)
combo_box.current=0


button2 = ttk.Button(win,text='close',command=win.destroy)
button2.grid(row=4,column=0)






win.mainloop()