import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num +=1
    prime_list.append(random_num)
print(prime_list)
 # 4. Get the smallest number from a list
def min_in_list(py_list):
    return min(py_list)

print(f"Minimum in the list: {min(prime_list)}")