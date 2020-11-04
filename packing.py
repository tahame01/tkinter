import tkinter as tk
from tkinter import ttk 


root = tk.Tk()

def button1():
    print(f"hello {input.get() or 'no name been given!'}")

input = tk.StringVar()

#check out ttk frame padding property!!
frame1 = ttk.Frame(root,padding=(10,10,20,20))
frame1.pack(fill='both')


frame2 = ttk.Frame(root,padding=(30,30))
frame2.pack(fill='both')



text_entry = ttk.Entry(frame1,width=20,textvariable=input)
text_entry.pack()
text_entry.focus()


button1 = tk.Button(frame2,text='click me',bg='green',fg='black',command=button1)
button1.pack(side='left',expand=True)



button2 = tk.Button(frame2,bg='red',text='click me')
button2.pack(side='left',expand=True)


root.mainloop()