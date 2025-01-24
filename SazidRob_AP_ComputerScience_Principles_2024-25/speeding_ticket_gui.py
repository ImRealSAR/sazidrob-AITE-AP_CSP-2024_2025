from tkinter import *

root = Tk()
root.geometry("800x800")
font = ("Helvetica", 16)

frame = Frame(root, width=800, height=800, bg="LightBlue")
frame.pack()

intro = Label(frame, text="Speeding ticket calculator", font=font)
intro.grid(row=0, column=1, pady=10)

speed_label = Label(frame, text="Enter speed: ", font=font)
speed_label.grid(row=1, column=0, padx=10, pady=10)

speed_entry = Entry(frame, font=font)
speed_entry.grid(row=1, column=1, padx=10, pady=10)

checkmark = Checkbutton(frame, text="Birthday", font=font)
checkmark.grid(row=2, column=1, pady=10)

root.mainloop()
