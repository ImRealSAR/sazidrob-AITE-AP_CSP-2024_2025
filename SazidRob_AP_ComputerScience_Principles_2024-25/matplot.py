import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


root=Tk()
root.title('School Data')
root.geometry('800x800')


e = 0
entries=[]
data_entries=[]
def add_entry():
   global e, entries, data_entries
   school_entry=Entry(root,width=20)
   school_entry.grid(row=e,column=1,sticky=W)   
   entries.append(school_entry)
   e += 1
   for i in range(len(entries)):
       school_label=Label(root,text="Enter Data Figure # " + str(i+1),width=15)
       school_label.grid(row=i,column=0,sticky=W)
   data_label=Entry(root,width=20)
   data_label.grid(row=e-1,column=3,sticky=W)
   data_entries.append(data_label)
   for i in range(len(data_entries)):
       school_label=Label(root,text="Enter Data Label " + str(i+1),width=15)
       school_label.grid(row=i,column=2,sticky=W)


def delete_row():
   global entries, data_entries
   entries.pop()
   data_entries.pop()


canvas = Canvas(root,width=400,height=400)
def create_graph():
   global entries, canvas
   entry_data = []
   data_labels = []
   fig=Figure(figsize= (5,5),dpi=100)
   l = len(entries) + 1
   for i in range(len(entries)):
       upd_entries = entries[i].get()
       entry_data.append(int(upd_entries))
   for i in range(len(data_entries)):
       upd_data_entries = data_entries[i].get
       data_labels.append(upd_data_entries)
  
   gen_data=np.array(entry_data)


   plot1=fig.add_subplot(111)
   plot1.scatter(data_labels,gen_data)
   canvas = FigureCanvasTkAgg(fig,master=root)
   canvas.draw()
   canvas.get_tk_widget().grid(row=e+1,column=0,sticky=E)


graph_button = Button(root, tex="Create Graph",width=15,command=create_graph).grid(row=e+1,column=4)
add_row_button = Button(root,text="Add Row",width=15,command=add_entry).grid(row=e+2,column=4)
delete_row = Button(root,text="Delete Row",width=15,command=delete_row).grid(row=e+3,column=4)

root.mainloop()