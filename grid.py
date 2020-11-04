import tkinter as tk 
from tkinter import ttk 


root = tk.Tk()
input = tk.StringVar()


def button1():
    print(f" hello {input.get() or 'not given any word'}")


root.columnconfigure(0, weight=1)
#root.rowconfigure(1, weight=1)


#check out ttk frame padding property!!
frame1 = ttk.Frame(root,padding=(20,10,20,10))
frame1.grid(sticky='EW')


frame2 = ttk.Frame(root,padding=(20,10,20,10))
frame2.grid(sticky='EW')

frame2.columnconfigure(0,weight=1)



label1 = ttk.Label(frame1,text='Name: ')
label1.grid(row=0,column=0)
label1.configure(background='red')

text_entry = ttk.Entry(frame1,width=15,textvariable=input)
text_entry.grid(row=0,column=1)
text_entry.focus()
# text_entry.columnconfigure(0,weight=1)

button1 = ttk.Button(frame1,text='submit',command=button1)
button1.grid(row=1,column=0)



button2 = ttk.Button(frame1,text='close',command=root.destroy)
button2.grid(row=1,column=1)








root.mainloop()