import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num +=1
    prime_list.append(random_num)
print(prime_list)
   # 2. Multiply stuff in list
def multiplying_list(py_list): 
    result = 1
    for item in py_list:
        result *= item
    return result 

print(f"Multiplication of the list: {multiplying_list(prime_list)}") 
