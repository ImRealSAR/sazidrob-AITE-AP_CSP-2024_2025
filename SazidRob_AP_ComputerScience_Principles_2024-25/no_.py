from tkinter import *

root = Tk()

root.geometry("800x800")
root.title("Ali loves kids and Aidan LOVES LOVES LOVES Meowskulls")

# Label 
label = Label(root, text="No", fg="Red")
label.grid(row=0, column=0, sticky=E)

# Entry box
num = StringVar()  # Corrected variable initialization
entry = Entry(root, textvariable=num, width=20)
entry.grid(row=0, column=1)

label1 = Label(root, text="Test")
label1.grid(row=1, column=0, sticky=E)

def click_button():
    label1.config(text="Button was clicked")

# Button
agree = Button(root, text="I Agree with GUI", command=click_button)
agree.grid(row=1, column=1)

# Slider
slider = []
for i in range(3):
    if i == 0:
        slider_widget = Scale(root, label="Red", from_=0, to=255, orient="horizontal")
    elif i == 1:
        slider_widget = Scale(root, label="Green", from_=0, to=255, orient="horizontal")
    else:
        slider_widget = Scale(root, label="Blue", from_=0, to=255, orient="horizontal")
    slider_widget.grid(row=i, column=2)
    slider.append(slider_widget)

# Checkbutton
cb_var = IntVar()  # Added a variable to store the state of the Checkbutton
cb = Checkbutton(root, text="Check me", variable=cb_var)  # Corrected "txt" to "text"
cb.grid(row=4, column=0)

# Radiobutton
rb_var = IntVar()  # Added a variable for the Radiobutton group
rb = Radiobutton(root, text="Radio me", variable=rb_var, value=1)
rb.grid(row=5, column=0)

# Launch GUI
root.mainloop()
