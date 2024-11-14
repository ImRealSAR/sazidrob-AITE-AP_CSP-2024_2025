import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num +=1
    prime_list.append(random_num)
print(prime_list)
    # 3. Get the highest number from a list
def max_in_list(py_list):
    return max(py_list)

print(f"Maximum in the list: {max_in_list(prime_list)}")