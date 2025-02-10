# # print(final_res)
# # n = 254
# # a = n // 16
# # b = n % 16
# # letts = ["A","B","C","D","E","F"]
# # nums = [10,11,12,13,14,15]
# # res = ""
# # for i in range(len(nums)):
# #     if a == nums[i]:
# #         a = letts[i]
# #     if b == nums[i]:
# #         b == letts[i]
# # res += str(a) + str(b)
# # if res[0] == "0":
# #     res = res[1:]
# # print (res)

# from tkinter import *

# root = Tk()
# root.geometry("1000x1000")

# operation = IntVar(root)

# frame = Frame(root, width=800, height=800)
# frame.pack()

# Label(frame, text="Title of GUI").pack()
# Label(frame, text="Label for Entry Box").pack()

# dec_entry = Entry(frame)
# dec_entry.pack()

# r1 = Radiobutton(frame, text="Decimal to Binary", value=1, variable=operation, command=lambda: print(dec_to_bin()))
# r1.pack()

# r2 = Radiobutton(frame, text="Decimal to Hexadecimal", value=2, variable=operation, command=lambda: print("Hex function placeholder"))
# r2.pack()

# Label(frame, text="Label for Results").pack()

# def dec_to_bin():
#     n = int(dec_entry.get())  # Convert input to integer
#     nums = []
#     final_res = ""
    
#     while n > 0:
#         nums.append(n % 2)
#         n = n // 2

#     for i in range(len(nums)-1, -1, -1):
#         final_res += str(nums[i])
    
#     return final_res

# root.mainloop()
from tkinter import *

root = Tk()
root.geometry("1000x1000")

operation = IntVar(root)

frame = Frame(root, width=800, height=800)
frame.pack()

Label(frame, text="Enter Decimal Number:").pack()
dec_entry = Entry(frame)
dec_entry.pack()

r1 = Radiobutton(frame, text="Decimal to Binary", value=1, variable=operation, command=lambda: select())
r1.pack()

r2 = Radiobutton(frame, text="Decimal to Hexadecimal", value=2, variable=operation, command=lambda: select())
r2.pack()

Label(frame, text="Result:").pack()
result_entry = Entry(frame)
result_entry.pack()

def dec_to_bin():
    n = int(dec_entry.get())
    if n == 0:
        return "0"
    nums = []
    final_res = ""
    while n > 0:
        nums.append(n % 2)
        n = n // 2
    for i in range(len(nums)-1, -1, -1):
        final_res += str(nums[i])
    return final_res

def dec_to_hex():
    n = int(dec_entry.get())
    if n == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        remainder = n % 16
        result = hex_digits[remainder] + result
        n = n // 16
    return result

def select():
    if operation.get() == 1:
        res = dec_to_bin()
    elif operation.get() == 2:
        res = dec_to_hex()
    else:
        res = ""
    result_entry.delete(0, END)
    result_entry.insert(0, res)

root.mainloop()
