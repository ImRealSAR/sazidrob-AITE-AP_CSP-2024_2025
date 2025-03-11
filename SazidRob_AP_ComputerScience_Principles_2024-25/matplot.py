import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title('School Data')
root.geometry('800x800')
root.configure(bg='black')

entries = []
data_entries = []

def add_entry():
    row = len(entries)
    Label(root, text=f"Data {row + 1}:", fg='lime', bg='black').grid(row=row, column=0, padx=5, pady=5, sticky=W)
    school_entry = Entry(root, width=15, bg='black', fg='lime', insertbackground='lime')
    school_entry.grid(row=row, column=1, padx=5, pady=5)
    entries.append(school_entry)
    
    Label(root, text=f"Label {row + 1}:", fg='lime', bg='black').grid(row=row, column=2, padx=5, pady=5, sticky=W)
    data_entry = Entry(root, width=15, bg='black', fg='lime', insertbackground='lime')
    data_entry.grid(row=row, column=3, padx=5, pady=5)
    data_entries.append(data_entry)

def delete_row():
    if entries and data_entries:
        entries.pop().destroy()
        data_entries.pop().destroy()

def create_graph(graph_type):
    if not entries or not data_entries:
        return
    
    entry_data = [int(entry.get()) for entry in entries if entry.get().isdigit()]
    data_labels = [label.get() for label in data_entries if label.get()]
    
    if len(entry_data) != len(data_labels) or not entry_data:
        return
    
    fig = Figure(figsize=(5, 4), dpi=100, facecolor='black')
    ax = fig.add_subplot(111)
    ax.set_facecolor('black')
    ax.tick_params(axis='both', colors='lime')
    ax.spines['bottom'].set_color('lime')
    ax.spines['left'].set_color('lime')
    
    if graph_type == "scatter":
        ax.scatter(data_labels, entry_data, color='lime', s=100, alpha=0.7)
        ax.set_title("Scatter Plot", color='lime')
    elif graph_type == "bar":
        ax.bar(data_labels, entry_data, color='lime', alpha=0.7)
        ax.set_title("Bar Graph", color='lime')
    
    ax.set_xlabel("Labels", color='lime')
    ax.set_ylabel("Values", color='lime')
    ax.grid(True, color='lime', linestyle='dashed', linewidth=0.5)
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=len(entries) + 1, column=0, columnspan=4, pady=10)

graph_button = Button(root, text="Create Scatter Plot", command=lambda: create_graph("scatter"), fg='lime', bg='black')
graph_button.grid(row=100, column=0, columnspan=2, pady=10, padx=5)

bar_button = Button(root, text="Create Bar Graph", command=lambda: create_graph("bar"), fg='lime', bg='black')
bar_button.grid(row=100, column=2, columnspan=2, pady=10, padx=5)

add_row_button = Button(root, text="Add Row", command=add_entry, fg='lime', bg='black')
add_row_button.grid(row=101, column=0, columnspan=2, pady=5)

delete_row_button = Button(root, text="Delete Row", command=delete_row, fg='lime', bg='black')
delete_row_button.grid(row=101, column=2, columnspan=2, pady=5)

root.mainloop()
