import random # random module is useful for this, because I don't know what numbers to work with
import math # in case i need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num += 1
    prime_list.append(random_num)
    random_num1 = random_num
    random_num1 += 1
    prime_list.append(random_num1)
    random_num += random_num1
print(prime_list)

def remove_duplicates(py_list):
    list_py = []
    for item in py_list:
        if item not in list_py:
            list_py.append(item)
    return list_py

print(f"List after removing duplicates: {remove_duplicates(prime_list)}")