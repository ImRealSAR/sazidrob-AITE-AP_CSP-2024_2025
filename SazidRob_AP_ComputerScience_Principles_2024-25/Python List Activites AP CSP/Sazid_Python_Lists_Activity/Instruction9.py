import random # In case I need random numbers
import math # In case I need it
random_num = random.randint(1, 21)
another_random_num = random.randint(1, 21)
prime_list = []
second_list = []
for update in range(7):
    random_num += 1
    prime_list.append(random_num)
    another_random_num += 1
    second_list.append(another_random_num)
print(prime_list)
print(second_list)
def common_num_check():
    for element in prime_list:
        if element not in range(len(second_list)):
            return True
        print("There is a common number!")
print(common_num_check())
