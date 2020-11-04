import tkinter as tk
from tkinter import ttk

root = tk.Tk()


#frame object will be packed later in the nest line as it behaves different!!!
frame1 = ttk.Frame(root)
frame1.pack(side='left',fill='both',expand=True)



label1=tk.Label(frame1,text='label 1',fg='white',bg='red').pack(side='top',expand=True,fill='both')
label2=tk.Label(frame1,text='label 2',fg='black',bg='yellow').pack(side='top',expand=True,fill='both')


button1 = tk.Button(root,text='exit',bg='red',fg='white').pack(side='left',expand=True,fill='both')


root.mainloop()