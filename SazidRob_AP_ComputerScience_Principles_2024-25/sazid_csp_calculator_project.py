# # This is a multi-purpose calculator for my AP Computer Science Principles project.
# # Import necessary modules/libraries from Python
import math
import random
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

def root(x,y): # Need button for this in the GUI
    if y == 2:
        return math.sqrt(x)
    elif y == 0:
        raise ValueError("You can't root using 0!")
    elif y == -1:
        return 1/x
    elif y == -2:
        return 1/math.sqrt(x)
    elif y <= -3:
        return 1/(x**(1/y))
    elif y == 1:
        return x
    elif x <= 0:
        raise ValueError("You can't root using negative numbers!")
    else:
        return x ** (1/y)

def dice(x,y): # GUI-compatible dice function
    if x != int(x) or y != int(y):
        raise ValueError("Dice sides and count must be whole numbers!")
    rolls = [random.randint(1, int(x)) for _ in range(int(y))]
    return sum(rolls)

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
        elif operation == "root":
            result = root(num1, num2)
        elif operation == "dice":
            result = dice(num1, num2)
        result_label.config(text=f"Result: {result}")
        history.append(f"{num1} {operation} {num2} = {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Clear the calculator inputs like a real one would do 
def clear_all():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result_label.config(text="Result: ")

# Open a new window to show the history of calculations that the user tried so far. This won't show old calculations if the user exits out and reruns.
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("300x300")
    history_window.configure(bg="white")
    
    tk.Label(history_window, text="Your Calculations History:", bg="white", font=("Arial", 12, "bold")).pack(pady=10)
    
    text_area = tk.Text(history_window, wrap="word", height=12, width=40)
    text_area.pack(padx=10, pady=5)
    
    for i in history:
        text_area.insert(tk.END, i + "\n")
    
    text_area.config(state="disabled")  # This (above) is so that user can’t type in it

# The main tKinter standard window
root = tk.Tk()
root.title("Calculator--By Sazid/SAR")
root.geometry("500x500")
root.configure(bg="black")

# Create input fields with added styling
tk.Label(root, text="Enter the first number:", bg="black", fg="white", font=("Helvetica", 10)).grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root, font=("Helvetica", 10), bd=2, relief="groove")
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Enter the second number:", bg="black", fg="white", font=("Helvetica", 10)).grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, font=("Helvetica", 10), bd=2, relief="groove")
entry2.grid(row=1, column=1, padx=5, pady=5)

# Create buttons for operations with improved styling
tk.Button(root, text="Add", command=lambda: calculate("add"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Divide", command=lambda: calculate("divide"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Modulo", command=lambda: calculate("modulo"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="Exponent", command=lambda: calculate("exponent"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Dice Roll", command=lambda: calculate("dice"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="Root", command=lambda: calculate("root"), bg="#004466", fg="white", font=("Helvetica", 10)).grid(row=5, column=1, padx=5, pady=5)

# Clear buton 
tk.Button(root, text="Clear", command=clear_all, bg="#660000", fg="white", font=("Helvetica", 10)).grid(row=6, column=0, padx=5, pady=5)

# Show history button
tk.Button(root, text="Show History", command=show_history, bg="#660000", fg="white", font=("Helvetica", 10)).grid(row=6, column=1, padx=5, pady=5)

# This is for the results to be shown to the calculator user. 
result_label = tk.Label(root, text="Result: ", bg="black", fg="lime", font=("Helvetica", 12, "bold"))
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
