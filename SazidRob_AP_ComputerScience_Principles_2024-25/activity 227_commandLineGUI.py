import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter.filedialog import asksaveasfilename
import platform

font_yes = ("Arial Black", 14)
blood_red_hex = "#880808"

def do_command(command):
    global command_textbox
    url_val = url_entry.get()  
    if len(url_val) == 0:
        url_val = "google.com"  
    system_os = platform.system()
    if command == "ping":
        p = subprocess.Popen(["ping", "-n" if system_os == "Windows" else "-c", "4", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif command == "nslookup":  
        p = subprocess.Popen(["nslookup", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif command == "traceroute":  
        p = subprocess.Popen(["tracert" if system_os == "Windows" else "traceroute", url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} to {url_val} is working....\n")
    command_textbox.update()
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results.decode())  
    command_textbox.insert(tk.END, cmd_errors.decode())  

root = tk.Tk()
frame_URL = tk.Frame(root, pady=10, bg="black")  
frame_URL.pack()

url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=(font_yes),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg=blood_red_hex,
    bg="black")
url_label.pack(side=tk.LEFT)

url_entry = tk.Entry(frame_URL, font=(font_yes))  
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack()

command_textbox = tksc.ScrolledText(root, height=10, width=100)
command_textbox.pack(pady=10)

ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", 
    command=lambda: do_command("ping"),
    compound="center",
    font=(font_yes),
    bd=0, 
    relief="flat",
    cursor="heart")
ping_btn.pack(side=tk.LEFT, padx=5)

ns_lookup = tk.Button(frame, text="NS Lookup", command=lambda: do_command("nslookup"))
ns_lookup.pack(side=tk.LEFT, padx=5)

otherbutton = tk.Button(frame, text="Other", command=lambda: do_command("traceroute"))  
otherbutton.pack(side=tk.LEFT, padx=5)

tracert = tk.Button(frame, text="Traceroute", command=lambda: do_command("traceroute"))
tracert.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(frame_URL, text="Save Output", command=lambda: asksaveasfilename(defaultextension='.txt', filetypes=(("Text files", "*.txt"), ("Python files", "*.py *.pyw"), ("All files", "*.*"))), font=(font_yes))
save_btn.pack(pady=5)

root.mainloop()
