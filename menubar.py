import tkinter as tk 
from tkinter import ttk 
from tkinter import Menu 
from tkinter import messagebox as msg 

root = tk.Tk()


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def _quit():
    root.quit()
    root.destroy()
    exit()

#Adding message box

def _message():
    # msg.showinfo('Hello buddy just trying to checkout the message box!!')
    msg.showwarning('Warning!!! Auchtung')



#Creating menubar
menu_bar = Menu(root)
root.config(menu=menu_bar)

#Creating file menu objects in menubar
file_menu = Menu(menu_bar,tearoff=0) #tearoff will tear off the line
file_menu.add_command(label='New')
file_menu.add_command(label='Home')
file_menu.add_separator()  #adding seperator
file_menu.add_command(label='Datasets')

##creating second data menu objects
data_menu = Menu(menu_bar,tearoff=0)
data_menu.add_command(label='Datasets')
data_menu.add_command(label='Graph')

#Creating exit menu
exit_menu = Menu(menu_bar,tearoff=0)
exit_menu.add_command(label='help',command=_message)
exit_menu.add_command(label='quit',command=_quit)

menu_bar.add_cascade(label='File',menu=file_menu)
menu_bar.add_cascade(label='Data',menu=data_menu)
menu_bar.add_cascade(label='Exit',menu=exit_menu)



root.mainloop()