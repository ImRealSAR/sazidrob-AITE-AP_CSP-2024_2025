# import subprocess
# import tkinter as tk
# import tkinter.scrolledtext as tksc
# from tkinter.filedialog import asksaveasfilename

# def do_command(command):
#     global command_textbox

#     url_val = url_entry.get()  
#     global p
#     if command == "ping":
#         p = subprocess.Popen(['ping', url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     elif command == "nslookup":  
#         p = subprocess.Popen(['nslookup', url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     elif command == "traceroute":  
#         p = subprocess.Popen(['traceroute', url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  ()
    

    
#     command_textbox.delete(1.0, tk.END)
#     command_textbox.insert(tk.END, f"{command} to {url_val} is working....\n")
#     command_textbox.update()

#     cmd_results, cmd_errors = p.communicate()
#     command_textbox.insert(tk.END, cmd_results.decode())  
#     command_textbox.insert(tk.END, cmd_errors.decode())  


# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# command_textbox = tksc.ScrolledText(frame, height=10, width=100)
# command_textbox.pack()

# ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", 
#     command=lambda: do_command("ping"),
#     compound="center",
#     font=("comic sans", 12),
#     bd=0, 
#     relief="flat",
#     cursor="heart")
# ping_btn.pack()

# ns_lookup = tk.Button(frame, text="NS Lookup", command=lambda: do_command("nslookup"))
# ns_lookup.pack()

# otherbutton = tk.Button(frame, text="other", command=lambda: do_command("traceroute"))  
# otherbutton.pack()

# tracert = tk.Button(root,text="traceart", command=lambda:do_command("ping"))
# tracert.pack()
# frame_URL = tk.Frame(root, pady=10, bg="black")  
# frame_URL.pack()

# def mSave():
#     filename = asksaveasfilename(defaultextension='.txt',
#                                  filetypes=(('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
#     if filename is None:
#         return
#     with open(filename, 'w') as file:
#         text_to_save = command_textbox.get("1.0", tk.END)
#         file.write(text_to_save)


# save_btn = tk.Button(frame_URL, text="Save Output", command=mSave, font=("comic sans", 12))
# save_btn.pack(pady=5)


# url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
#     compound="center",
#     font=("comic sans", 14),
#     bd=0, 
#     relief=tk.FLAT, 
#     cursor="heart",
#     fg="mediumpurple3",
#     bg="black")
# url_label.pack(side=tk.LEFT)

# url_entry = tk.Entry(frame_URL, font=("comic sans", 14))  
# url_entry.pack(side=tk.LEFT)

# frame = tk.Frame(root, bg="black")  
# frame.pack()

# root.mainloop()

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox
    url_val = url_entry.get()
    global p
    if command == "ping":
        p = subprocess.Popen(['ping', url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif command == "nslookup":
        p = subprocess.Popen(['nslookup', url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif command == "traceroute":
        p = subprocess.Popen(['traceroute', url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Clear textbox and insert initial message.
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"Executing '{command}' on {url_val}...\n")
    command_textbox.update()
    
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results.decode())
    command_textbox.insert(tk.END, cmd_errors.decode())

def mSave():
    filename = asksaveasfilename(defaultextension='.txt',
                                 filetypes=(('Text files', '*.txt'), 
                                            ('Python files', '*.py;*.pyw'), 
                                            ('All files', '*.*')))
    if not filename:
        return
    with open(filename, 'w') as file:
        text_to_save = command_textbox.get("1.0", tk.END)
        file.write(text_to_save)

# Set up the main window.
root = tk.Tk()
root.title('Network Command Executor')
root.configure(bg="#2e2e2e")
root.geometry("900x700")

# Top frame with a title.
top_frame = tk.Frame(root, bg="#2e2e2e")
top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
title_label = tk.Label(top_frame, text="Network Command Executor", 
                       font=("Helvetica", 18, "bold"), fg="cyan", bg="#2e2e2e")
title_label.pack()

# Frame for the command output.
output_frame = tk.Frame(root, bg="#1e1e1e")
output_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
command_textbox = tksc.ScrolledText(output_frame, height=15, width=100, wrap=tk.WORD, 
                                    bg="#000000", fg="lime", font=("Consolas", 12))
command_textbox.pack(fill=tk.BOTH, expand=True)

# Frame for command buttons.
button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
ping_btn = tk.Button(button_frame, text="Ping URL", 
                     command=lambda: do_command("ping"),
                     font=("Verdana", 12), fg="white", bg="#007acc", bd=2, relief="ridge")
ping_btn.grid(row=0, column=0, padx=5, pady=5)
ns_lookup_btn = tk.Button(button_frame, text="NS Lookup", 
                          command=lambda: do_command("nslookup"),
                          font=("Verdana", 12), fg="white", bg="#007acc", bd=2, relief="ridge")
ns_lookup_btn.grid(row=0, column=1, padx=5, pady=5)
trace_btn = tk.Button(button_frame, text="Traceroute", 
                      command=lambda: do_command("traceroute"),
                      font=("Verdana", 12), fg="white", bg="#007acc", bd=2, relief="ridge")
trace_btn.grid(row=0, column=2, padx=5, pady=5)
# Additional button (for example, another ping option)
tracert_btn = tk.Button(button_frame, text="Trace Ping", 
                        command=lambda: do_command("ping"),
                        font=("Verdana", 12), fg="white", bg="#007acc", bd=2, relief="ridge")
tracert_btn.grid(row=0, column=3, padx=5, pady=5)

# Frame for URL entry and saving the output.
entry_frame = tk.Frame(root, bg="#2e2e2e")
entry_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
url_label = tk.Label(entry_frame, text="Enter URL:", font=("Verdana", 14), 
                     fg="orange", bg="#2e2e2e")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(entry_frame, font=("Verdana", 14), width=30, bd=2, relief="sunken")
url_entry.grid(row=0, column=1, padx=5, pady=5)
save_btn = tk.Button(entry_frame, text="Save Output", command=mSave, font=("Verdana", 12), 
                     fg="white", bg="#007acc", bd=2, relief="ridge")
save_btn.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()