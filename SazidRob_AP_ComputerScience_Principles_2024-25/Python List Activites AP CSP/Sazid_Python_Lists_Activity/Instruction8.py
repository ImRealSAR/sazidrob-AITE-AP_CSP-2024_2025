import random  # In case I need random numbers
import math  # In case I need it
# random_num = random.randint(1, 21)
prime_list = ['Never', 'Gonna', 'Give', 'You', 'Up']
# for update in range(7):
#     prime_list.append(random_num)
print(prime_list)
n = 4
long_words = []
for word in prime_list:
    if len(word) > n:
        long_words.append(word)
        long_words.sort() # Just to make it alphabetically correct lol
print(long_words)
