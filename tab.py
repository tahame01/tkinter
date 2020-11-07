import tkinter as tk 
from tkinter import ttk 
from tkinter import Menu 


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


tab_controll = ttk.Notebook(root)
tab1 = ttk.Frame(tab_controll)
tab2 = ttk.Frame(tab_controll)
tab3 = ttk.Frame(tab_controll)
tab_controll.add(tab1,text='Tab 1')
tab_controll.add(tab2,text='Tab 2')
tab_controll.add(tab3,text='Tab 3')
tab_controll.pack(expand=1,fill='both')

label1 = tk.Label(tab1,bg='red').pack(expand=1,fill='both')
label2 = tk.Label(tab2,bg='green').pack(expand=1,fill='both')
label1 = tk.Label(tab3,bg='yellow').pack(expand=1,fill='both')








root.mainloop()