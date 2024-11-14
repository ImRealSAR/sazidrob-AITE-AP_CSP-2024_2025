import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num +=1
    prime_list.append(random_num)
print(prime_list)
    # 1. Summing lists that user inputs
def sum_of_list(py_list):
    return sum(py_list)

print(f" Sum of the list: {sum_of_list(prime_list)}")