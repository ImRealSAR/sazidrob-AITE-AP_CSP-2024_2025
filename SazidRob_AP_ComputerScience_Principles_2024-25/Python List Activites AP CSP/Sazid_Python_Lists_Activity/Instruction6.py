import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num +=1
    prime_list.append(random_num)
print(prime_list)
# 6. Check if a list is empty or not
def list_empty(py_list):
    for element in range(len(py_list)):
        element = py_list[element]
    if element > 0:
        return ("No")
    else:
        return ("Yes")    

print(f"Is the list empty?: {list_empty(prime_list)}")