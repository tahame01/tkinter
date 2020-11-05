import pandas as pd
from pandastable import Table
from tkinter import * 
# Load CSV using Pandas
from pandas import read_csv
import datatable as dt


# filename = 'pima-indians-diabetes.data.csv'
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# data = read_csv(filename, names=names)
# data1=data.head()
df = dt.fread('pima-indians-diabetes.data.csv')
pandas_df = df.to_pandas()

root=Tk()
frame = Frame(root)
frame.pack()

# table=Table(frame,dataframe=data1,showtoolbar=True,showstatusbar=True)
table=Table(frame,dataframe=pandas_df,showtoolbar=True,showstatusbar=True)

table.show()

root.mainloop()