from tkinter import *

root = Tk()
root.geometry("200x200")
root.configure(bg="black")
font = ("Helvetica", 16)

login_frame = Frame(root, width=200, height=200, bg="black")
login_frame.grid(row=0, column=0, sticky="news")
username_label = Label(login_frame, text="Username: ", font=font, fg="green", bg="black")
username_label.pack(padx=100, pady=20)
username_entry = Entry(login_frame, width=25, fg="green", bg="black", insertbackground="green")
username_entry.pack(padx=100, pady=20)
password_label = Label(login_frame, text="Password: ", font=font, fg="green", bg="black")
password_label.pack(padx=100, pady=20)
password_entry = Entry(login_frame, width=25, show="*", fg="green", bg="black", insertbackground="green")
password_entry.pack(padx=100, pady=20)

def pass_create():
    global username, password
    print("Username must be 8 characters")
    space = True
    while len(username) < 8 or space == False:
        username = input("Enter username: ")
        for i in username:
            if i == " ":
                space = False
                break
            else:
                space = True
    print("Password must be 8 characters consisting of letters and numbers")

    passworddig = False
    passalph = False
    space = True

    while len(password) < 8 or passalph == False or passworddig == False or space == False:
        passworddig = False
        passalph = False

        password = input("Enter password: ")
        for i in username:
            if i == " ":
                space = False
                break
            else:
                space = True

        for i in password:
            if i.isdigit():
                passworddig = True
            if i.isalpha():
                passalph = True
    print("Username and Password accepted")

username = ""
password = ""

def login():
    if username_entry.get() == username and password_entry.get() == password:
        auth_frame.tkraise()
    else:
        fail_frame.tkraise()

submit = Button(login_frame, text="Login", font=font, command=login, fg="green", bg="black")
submit.pack(padx=100, pady=20)
auth_frame = Frame(root, width=200, height=200, bg="black")
auth_frame.grid(row=0, column=0, sticky="news")
fail_frame = Frame(root, width=200, height=200, bg="black")
fail_frame.grid(row=0, column=0, sticky="news")
fail_label = Label(auth_frame, text="you fired", font=font, fg="green", bg="black")
fail_label.grid(row=0, column=0)
auth_label = Label(auth_frame, text="you hired", font=font, fg="green", bg="black")
auth_label.grid(row=0, column=0)
login_frame.tkraise()

root.mainloop()