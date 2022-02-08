
"""
this program will aks the user for a number to factor and print oyt all the sorted factors of that number. It will ask the user for numbers until they want to quit.
"""
#get the factors for a number and retuerns them as a sorted lsit
def factors(number):
    final_factors=[number]
    for i in range(1, int(number/2)+1):
        if number % i == 0: #i is a facor of number
            final_factors.append(i)


            print(final_factors)



user_number=int(input("pkease enter number:"))
factors(user_number)
