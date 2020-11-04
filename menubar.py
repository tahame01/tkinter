import tkinter as tk 
from tkinter import ttk 
from tkinter import Menu 


root = tk.Tk()


#Creating menubar
menu_bar = Menu(root)
root.config(menu=menu_bar)

#Creating objects in menubar
file_menu = Menu(menu_bar)
file_menu.add_command(label='New')
file_menu.add_command(label='Home')
file_menu.add_separator()
file_menu.add_command(label='Datasets')

menu_bar.add_cascade(label='File',menu=file_menu)





root.mainloop()