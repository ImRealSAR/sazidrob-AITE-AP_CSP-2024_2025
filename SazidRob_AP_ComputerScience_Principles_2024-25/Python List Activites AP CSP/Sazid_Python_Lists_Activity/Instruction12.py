import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
prime_list = []
for update in range(7):
    random_num += 1
    prime_list.append(random_num)
print(prime_list)
# 12. Turn every item in a list into its square
def square_list(py_list):
    return [x ** 2 for x in py_list]

print(f"List with squared values: {square_list(prime_list)}")