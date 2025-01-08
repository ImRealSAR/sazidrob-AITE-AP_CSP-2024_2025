# Functions
def primes(n):
    if n < 2: 
        return False
    for i in range(2, n): 
        if n % i == 0:
            return False 
    return True

def find_primes(n):
    if primes(n):
        return "Yes, is prime." 
    else:
        return "No, is not prime."

def number_of_primes(start, stop):
    primes_list = []
    for i in range(start, stop + 1):
        if primes(i): 
            primes_list.append(i)

    for prime in primes_list:
        print(prime, end=", ")  
    print("\nYou have this many prime numbers:" + str(len(primes_list)))  



#M ain
#num_1 = int(input("Enter a whole number: "))
#num_2 = int(input("Enter a whole number: "))

print(find_primes(7))
#number_of_primes(num_1,num_2)
