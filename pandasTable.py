import pandas as pd
from pandastable import Table
from tkinter import * 
# Load CSV using Pandas
from pandas import read_csv
import datatable as dt


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# filename = 'pima-indians-diabetes.data.csv'
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# data = read_csv(filename, names=names)
# data1=data.head()
df = dt.fread('pima-indians-diabetes.data.csv')
pandas_df = df.to_pandas()

root=Tk()
frame = Frame(root)


# table=Table(frame,dataframe=data1,showtoolbar=True,showstatusbar=True)
table=Table(frame,dataframe=pandas_df,showtoolbar=True,showstatusbar=True)
table.cellbackgr ='powderblue'
table.grid_color ='red'
table.show()

frame.pack()


root.mainloop()

# {'align': 'w',
#  'cellbackgr': '#F4F4F3',
#  'cellwidth': 80,
#  'colheadercolor': '#535b71',
#  'floatprecision': 2,
#  'font': 'Arial',
#  'fontsize': 12,
#  'fontstyle': '',
#  'grid_color': '#ABB1AD',
#  'linewidth': 1,
#  'rowheight': 22,
#  'rowselectedcolor': '#E4DED4',
#  'textcolor': 'black'}