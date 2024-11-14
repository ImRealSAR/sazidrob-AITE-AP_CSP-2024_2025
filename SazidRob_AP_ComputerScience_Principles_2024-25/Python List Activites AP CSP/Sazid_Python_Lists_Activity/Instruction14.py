import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num += 1
    prime_list.append(random_num)
    prime_list.append(20)
    prime_list.sort()
print(prime_list)
# 14. Remove all occurrences of 20 from a list
def remove_all_20(py_list):
    while 20 in py_list:
        py_list.remove(20)
    return py_list
remove_all_20(prime_list)
print(f"List after removing all 20s: {prime_list}")