from tkinter import *

# Create main window
root = Tk()
root.geometry("800x800")
root.title("Speeding Ticket Calculator")
font = ("Helvetica", 16)

frame = Frame(root, width=800, height=800, bg="LightBlue")
frame.pack()

# Title label
intro = Label(frame, text="Speeding Ticket Calculator", font=("Helvetica", 20, "bold"), bg="LightBlue")
intro.grid(row=0, column=0, columnspan=2, pady=20)

# speed label & entry
speed_label = Label(frame, text="Enter speed in mph:", font=font, bg="LightBlue")
speed_label.grid(row=1, column=0, padx=10, pady=10)
speed_entry = Entry(frame, font=font, width=25)
speed_entry.grid(row=1, column=1, padx=10, pady=10)
limit_label = Label(frame, text="Enter speed limit in mph:", font=font, bg="LightBlue")
limit_label.grid(row=2, column=0, padx=10, pady=10)
limit_entry = Entry(frame, font=font, width=25)
limit_entry.grid(row=2, column=1, padx=10, pady=10)

# birthday checkbox
birthday_check = Checkbutton(frame, text="Birthday?", font=font, bg="LightBlue")
birthday_check.grid(row=3, column=0, columnspan=2, pady=10)

# Slider for fine adjustment
fine_label = Label(frame, text="Fine Adjustment:", font=font, bg="LightBlue")
fine_label.grid(row=4, column=0, padx=10, pady=10)
fine_slider = Scale(frame, from_=0, to=500, orient="horizontal", font=font, length=300)
fine_slider.grid(row=4, column=1, padx=10, pady=10)

# Slider for how bad the situation at hand is
severity_label = Label(frame, text="Severity Level:", font=font, bg="LightBlue")
severity_label.grid(row=5, column=0, padx=10, pady=10)
severity_slider = Scale(frame, from_=1, to=10, orient="horizontal", font=font, length=300)
severity_slider.grid(row=5, column=1, padx=10, pady=10)

# compute your total fine
def calculate_results():
    speed = int(speed_entry.get())
    limit = int(limit_entry.get())
    fine_adjustment = fine_slider.get()
    severity = severity_slider.get()
    
    if speed <= limit:
        result_text = "You are within the speed limit. No ticket!"
    else:
        base_fine = (speed - limit) * 10
        total_fine = base_fine + fine_adjustment + (severity * 5)
        result_text = f"You were speeding! Fine: ${total_fine:.2f}"
    
    result_label.config(text=result_text, fg="green")

# compute button
calculate_button = Button(frame, text="Calculate Results", font=font, command=calculate_results, bg="SkyBlue")
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)
result_label = Label(frame, text="", font=font, bg="LightBlue")
result_label.grid(row=7, column=0, columnspan=2, pady=20)

root.mainloop()
