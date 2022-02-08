"""
a user will tell us a number and we will tell them if it is prime or not
Author: jonah Henschel
"""

# take an input from the user
number=int(input("please enter your number:"))
# check if divisible by 2
prime = True


if number % 2 == 0:
    print("this is  not prime")
    prime = False
else:
# loop through numbers up to input divied by two
    for i in range(3, number, 2):

    # check if its divisible by current number
    if number % i == 0:
        print("not prime")
        prime = False
        break


# if at end of loop there is no factor, print that it is prime
if prime:
    print("this number is prime ")





#if_prime will return true if number is prime and false if it is not
def is_prime(number):
    prime = True
    if number % 2 == 0:
        print("this is  not prime")
        return False
    else:
        # loop through numbers up to input divied by two
        for i in range(3, number, 2):

        # check if its divisible by current number
        if number % i == 0:
        print("not prime")
        return False

    # if at end of loop there is no factor, print that it is prime
    if prime:
        print("this number is prime ")
        return True

number=int(input("please enter your number:"))
is_prime(number)