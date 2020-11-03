import tkinter as tk
from tkinter import ttk 

root = tk.Tk()

user_name=tk.StringVar()



def button1():
    print(f"Hello{user_name.get() or 'world'} ") #Check this conditioning in format operator!!



label1 = ttk.Label(root,text='Your name:')
label1.pack(side='left',padx=(0,20))#using padding with pack------padx/pady
username = ttk.Entry(width=20,textvariable=user_name)# catching the entry with textvariable------
username.pack(side='left')
username.focus()



button1 = ttk.Button(root,text='click me',command=button1,padding=(10,20))#using padding inside ttk
button1.pack(side='top',fill='x',expand=True)
button2 = ttk.Button(root,text='exit',command=root.destroy)
button2.pack(side='left',fill='y')




root.mainloop()
