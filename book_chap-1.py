import tkinter as tk
from tkinter import ttk



win = tk.Tk()
win.title('test window')

# name = tk.StringVar()
# number = tk.StringVar()
# number = tk.IntVar()

# def clicked():
    #  label1.configure(text='Hello '+ name.get(),background='yellow')
    #  button1.configure(state='disabled')
    #  button1.configure(text='cant click me now')
    #  print(number.get())


# label1 = ttk.Label(win,text='Please input your name please ')
# label1.grid(row=0,column=0)

# text_entry = ttk.Entry(win,width=12,textvariable=name)
# text_entry.grid(row=1,column=0)
# text_entry.focus()

# check_box1 = tk.Checkbutton(win,text='checked',state='disabled')
# check_box1.select()
# check_box1.grid(row=0,column=0)

# check_box2 = tk.Checkbutton(win,text='check it',varible=number)
# check_box2.deselect()
# check_box2.grid(row=0,column=1)

#ttk button don't have background property
# button1 = ttk.Button(win,text='submit')
# button1.grid(row=2,column=0)

# combo_box = ttk.Combobox(text='select a number:',values=(1,2,3,4),textvariable=number)
# combo_box.grid(row=3,column=0)
# combo_box.current(0)


# button2 = ttk.Button(win,text='close',command=win.destroy)
# button2.grid(row=4,column=0)


color1='red'
color2='green'
color3='blue'

def rad_func():
    if rad_var.get()==1:win.configure(background=color1)
    elif rad_var.get()==2:win.configure(background=color2)
    else: win.configure(background=color3)



rad_var = tk.IntVar()

rad_button1 = tk.Radiobutton(win,text=color1,value=1,variable=rad_var,command=rad_func)
rad_button1.grid(row=0,column=0)
rad_button2 = tk.Radiobutton(win,text=color2,value=2,variable=rad_var,command=rad_func)
rad_button2.grid(row=0,column=1)
rad_button3 = tk.Radiobutton(win,text=color3,value=3,variable=rad_var,command=rad_func)
rad_button3.grid(row=0,column=2)

win.mainloop()