
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
import os
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox, url_entry

    url_val = url_entry.get()
    if len(url_val) == 0:
        url_val = "::1" 
   
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} working....\n")
    command_textbox.update()

    if os.name == 'nt':  
        if command == "ping":
            p = subprocess.Popen(f"ping {url_val}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        elif command == "nslookup":
            p = subprocess.Popen(f"nslookup {url_val}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        elif command == "tracert":
            p = subprocess.Popen(f"tracert {url_val}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    else: 
        if command == "ping":
            p = subprocess.Popen(["ping", "-c", "4", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif command == "nslookup":
            p = subprocess.Popen(["nslookup", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif command == "traceroute":
            p = subprocess.Popen(["traceroute", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    cmd_results, cmd_errors = p.communicate()


    command_textbox.insert(tk.END, cmd_results.decode())
    command_textbox.insert(tk.END, cmd_errors.decode())

def mSave():

    filename = asksaveasfilename(defaultextension='.txt', filetypes=(('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
    if not filename:
        return  

    with open(filename, mode='w') as file:
        text_to_save = command_textbox.get("1.0", tk.END)
        file.write(text_to_save)

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

url_entry = tk.Entry(frame_URL, font=("comic sans", 14))
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root, bg="black")
frame.pack()

def on_enter(event):
    event.widget.config(bg="#880808")

def on_leave(event):
    event.widget.config(bg="#880808")

ping_button = tk.Button(frame, text="Ping URL", command=lambda: do_command("ping"), bg="#880808")
ping_button.pack(pady=5)
ping_button.bind("<Enter>", on_enter)
ping_button.bind("<Leave>", on_leave)

nslookup_button = tk.Button(frame, text="NSLookup URL", command=lambda: do_command("nslookup"), bg="#880808")
nslookup_button.pack(pady=5)
nslookup_button.bind("<Enter>", on_enter)
nslookup_button.bind("<Leave>", on_leave)

tracert_button = tk.Button(frame, text="Traceroute URL", command=lambda: do_command("tracert" if os.name == 'nt' else "traceroute"), bg="#880808")
tracert_button.pack(pady=5)
tracert_button.bind("<Enter>", on_enter)
tracert_button.bind("<Leave>", on_leave)

save_button = tk.Button(frame, text="Save Output", command=mSave, bg="#880808")
save_button.pack(pady=5)
save_button.bind("<Enter>", on_enter)
save_button.bind("<Leave>", on_leave)

command_textbox = tksc.ScrolledText(frame, height=10, width=100, font=("comic sans", 12), bg="lightgray", fg="black")
command_textbox.pack()

root.mainloop()




