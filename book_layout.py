import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

button_frame = ttk.LabelFrame(root,text='this is label frame')
button_frame.grid(column=0,row=7)


label1 = ttk.Label(button_frame,text='label1').grid(row=0,column=0)
label2 = ttk.Label(button_frame,text='label2').grid(row=0,column=1)
label3 = ttk.Label(button_frame,text='label3').grid(row=0,column=2)













root.mainloop()