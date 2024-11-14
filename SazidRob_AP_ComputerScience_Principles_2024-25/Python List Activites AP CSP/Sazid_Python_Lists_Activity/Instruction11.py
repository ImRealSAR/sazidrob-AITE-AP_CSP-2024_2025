import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num += 1
    prime_list.append(random_num)
print(prime_list)
# 11. Reverse a list
def reverse_list(py_list):
    py_list.reverse()
    return py_list

print(f"Reversed list: {reverse_list(prime_list)}")