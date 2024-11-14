import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num +=1
    prime_list.append(random_num)
print(prime_list)
# 7. Clone the list
def clone_list(py_list):
    return py_list.copy()

perfectClone_list = clone_list(prime_list)
print(f"Cloned list: {(perfectClone_list)}")