import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

button_frame = ttk.LabelFrame(root,text='')
button_frame.grid(column=0,row=7,padx=40,pady=40)

# sticky property will act like text-align property


# label1 = ttk.Label(button_frame,text='label1').grid(row=0,column=0)
# label2 = ttk.Label(button_frame,text='label2').grid(row=0,column=1)
# label3 = ttk.Label(button_frame,text='label3').grid(row=0,column=2)


label1 = ttk.Label(button_frame,text='long labels label1').grid(row=0,column=0)
label2 = ttk.Label(button_frame,text='label2').grid(row=1,column=0,sticky=tk.W) #right align
label3 = ttk.Label(button_frame,text='label3').grid(row=2,column=0)

# The grid_configure() function enables us to modify the UI elements before the main
# The winfo_children() function returns a list of all the children belonging to the
# buttons_frame variable. This enables us to loop through them and assign the padding to
# each label.


# loop displays them. 
for child in button_frame.winfo_children():
    child.grid_configure(padx=20,pady=20)





root.mainloop()