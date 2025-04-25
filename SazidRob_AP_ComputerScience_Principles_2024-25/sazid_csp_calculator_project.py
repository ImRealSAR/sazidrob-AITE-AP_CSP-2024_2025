# # This is a multi-purpose calculator made by me (Sazid/SAR) for my AP Computer Science Principles project.
# # Import necessary modules/libraries from Python
import math
import random #(come back to this later to make random number generator and dice roll)
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from fractions import Fraction

# Keeps track of all previous calculations
history = []

# Functions for each mathematical operation
def is_number(value):
    try:
        float(Fraction(value))
        return True
    except ValueError:
        return False

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
        
def modulo(x, y):
    return x % y

def exponent(x, y):
    return x ** y

# Function to perform the said operations user clicks 
def calculate(operation):
    num1 = entry1.get()
    num2 = entry2.get()
    if not is_number(num1) or not is_number(num2):
        messagebox.showerror("Invalid input", "Please enter valid numbers")
        return
    num1 = float(Fraction(num1))
    num2 = float(Fraction(num2))
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "modulo":
            result = modulo(num1, num2)
        elif operation == "exponent":
            result = exponent(num1, num2)
        result_label.config(text=f"Result: {result}")
        history.append(f"{num1} {operation} {num2} = {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Clear the calculator inputs like a real one would do 
def clear_all():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result_label.config(text="Result: ")

# Open a new window to show the history of calculations
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("300x300")
    history_window.configure(bg="white")

    tk.Label(history_window, text="Previous Calculations:", bg="white", font=("Arial", 12, "bold")).pack(pady=10)

    text_area = tk.Text(history_window, wrap="word", height=12, width=40)
    text_area.pack(padx=10, pady=5)

    for item in history:
        text_area.insert(tk.END, item + "\n")

    text_area.config(state="disabled")  # So user can’t type in it

# Create main window
root = tk.Tk()
root.title("Calculator--By Sazid/SAR")
root.geometry("500x500")
root.configure(bg="black")

# Create input fields
tk.Label(root, text="Enter the first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create buttons for operations
tk.Button(root, text="Add", command=lambda: calculate("add")).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).grid(row=3, column=0)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).grid(row=3, column=1)
tk.Button(root, text="Modulo", command=lambda: calculate("modulo")).grid(row=4, column=0)
tk.Button(root, text="Exponent", command=lambda: calculate("exponent")).grid(row=4, column=1)

# Clear buton 
tk.Button(root, text="Clear", command=clear_all).grid(row=6, column=0)

# Show history button
tk.Button(root, text="Show History", command=show_history).grid(row=6, column=1)

# Results isplayed here
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
# This is a multi-purpose calculator made by me (Sazid/SAR) for my AP Computer Science Principles project.
