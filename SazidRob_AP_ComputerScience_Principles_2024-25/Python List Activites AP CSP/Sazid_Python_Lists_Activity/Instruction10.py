import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num += 1
    prime_list.append(random_num)
print(prime_list)
# 10. Remove the 0th, 4th, and 5th elements from a list
def remove_elements(py_list):
    py_list.pop(0)
    py_list.pop(3)
    py_list.pop(4)
    return py_list

print(f"List after removing elements: {remove_elements(prime_list)}")