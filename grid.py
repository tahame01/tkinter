import tkinter as tk 
from tkinter import ttk 


root = tk.Tk()


#check out ttk frame padding property!!
frame1 = tk.Frame(root,bg='yellow')
frame1.grid(row=0,column=7)

#frame1.columnconfigure(0,weight=1)
frame2 = tk.Frame(root,bg='green')
frame2.grid(row=1,column=4)

label1 = tk.Label(frame1,text='Label1',bg='blue')
label1.grid(row=0,column=4)

# text_entry = ttk.Entry(frame1,width=20,textvariable=input)
# text_entry.grid(row=1,column=2)
# text_entry.focus()
# text_entry.columnconfigure(0,weight=1)

# button1 = tk.Button(frame2,text='click me',bg='green',fg='black')
# button1.grid(row=1,column=1)



# button2 = tk.Button(frame2,bg='red',text='click me')
# button2.grid(row=1,column=2)









root.mainloop()