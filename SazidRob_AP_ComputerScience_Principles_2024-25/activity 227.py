
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
import os
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox, url_entry

    # Get the URL or IP from the input field, default to "::1" (localhost) if empty
    url_val = url_entry.get()
    if len(url_val) == 0:
        url_val = "::1"  # Default to localhost if no URL is entered
   
    # Clear the text box and show a working message
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} working....\n")
    command_textbox.update()

    # Execute the appropriate command based on the OS
    if os.name == 'nt':  # Windows
        if command == "ping":
            p = subprocess.Popen(f"ping {url_val}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        elif command == "nslookup":
            p = subprocess.Popen(f"nslookup {url_val}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        elif command == "tracert":
            p = subprocess.Popen(f"tracert {url_val}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    else:  # Linux/macOS
        if command == "ping":
            p = subprocess.Popen(["ping", "-c", "4", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif command == "nslookup":
            p = subprocess.Popen(["nslookup", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif command == "traceroute":
            p = subprocess.Popen(["traceroute", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the command output and errors
    cmd_results, cmd_errors = p.communicate()

    # Display the command output and errors in the text box
    command_textbox.insert(tk.END, cmd_results.decode())
    command_textbox.insert(tk.END, cmd_errors.decode())

def mSave():
    # Open save dialog to choose a file location
    filename = asksaveasfilename(defaultextension='.txt', filetypes=(('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
    if not filename:
        return  # Do nothing if no file is selected

    # Write the output from the text box to the selected file
    with open(filename, mode='w') as file:
        text_to_save = command_textbox.get("1.0", tk.END)
        file.write(text_to_save)

# Initialize the main window
root = tk.Tk()
root.title("Command Line Tool") 
root.config(bg="black") 

# URL input section
frame_URL = tk.Frame(root, pady=10, bg="black")
frame_URL.pack()

# Label for URL input
url_label = tk.Label(frame_URL, text="Enter a URL or IP address: ",
    font=("comic sans", 14),
    fg="#880808",
    bg="black")
url_label.pack(side=tk.LEFT)

# Input field for URL
url_entry = tk.Entry(frame_URL, font=("comic sans", 14))
url_entry.pack(side=tk.LEFT)

# Main frame for buttons and output box
frame = tk.Frame(root, bg="black")
frame.pack()

# Function to change button color on hover
def on_enter(event):
    event.widget.config(bg="#880808")

def on_leave(event):
    event.widget.config(bg="#880808")

# Create buttons for commands and apply hover effects
ping_btn = tk.Button(frame, text="Ping URL", command=lambda: do_command("ping"), bg="#880808")
ping_btn.pack(pady=5)
ping_btn.bind("<Enter>", on_enter)
ping_btn.bind("<Leave>", on_leave)

nslookup_btn = tk.Button(frame, text="NSLookup URL", command=lambda: do_command("nslookup"), bg="#880808")
nslookup_btn.pack(pady=5)
nslookup_btn.bind("<Enter>", on_enter)
nslookup_btn.bind("<Leave>", on_leave)

tracert_btn = tk.Button(frame, text="Traceroute URL", command=lambda: do_command("tracert" if os.name == 'nt' else "traceroute"), bg="#880808")
tracert_btn.pack(pady=5)
tracert_btn.bind("<Enter>", on_enter)
tracert_btn.bind("<Leave>", on_leave)

save_btn = tk.Button(frame, text="Save Output", command=mSave, bg="#880808")
save_btn.pack(pady=5)
save_btn.bind("<Enter>", on_enter)
save_btn.bind("<Leave>", on_leave)

# Output text box for displaying command results
command_textbox = tksc.ScrolledText(frame, height=10, width=100, font=("comic sans", 12), bg="lightgray", fg="black")
command_textbox.pack()

# Run the Tkinter event loop
root.mainloop()




