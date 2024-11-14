import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num += 1
    prime_list.append(random_num)
print(prime_list)
# 13. Replace the first occurrence of 20 with 200 in a list
def replace_20(py_list):
    for i in range(len(py_list)):
        if py_list[i] == 20:
            py_list[i] = 200
    return py_list 

print(f"The list after replacing first 20 with 200: {replace_20(prime_list)}")