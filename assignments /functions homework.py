
"""
Functions Practice

** Functions with no parameters and no return value **
1.  Write a function called dice_roll that will print the result of one random 6-sided dice roll.
2.  Write a function called tell_me_a_joke that will randomly generate a joke and print it.
3.  Write a function called current_date_and_time that will print out the current date and time
    in a nicely formatted way.
"""
import random


def dice_roll():
    return random.randint(1,6)


def tell_me_a_joke():
    jokes=[
        'why did the bike  fall over? it was two tired',
        'what is a snakes favorite school subject? hissstory',
        'which school supply is the king of the classroom? the ruler']
    index=random.randint(0,2)
    return jokes[index]



"""
** Functions with parameter(s), but no return value **
1.  Write a function called is_even that will accept a number as a parameter.
    It should print out "even" if the function is even, and "odd" if it is odd.
2.  Write a function called max that will accept three numbers as parameters.
    It should find the max of the three numbers and print it out.
3.  Write a function called list_sum that will accept a list of numbers as a parameter.
    It should sum up all the numbers in the list and print the sum.

"""
def maxnum(a,b,c):
    return max(a,b,c)
def list_sum(a):
    return  sum(a)


"""
** Functions with parameter(s) and a return value **
1.  Write a function called in_range that will check whether or not a number falls within a range.
    The function should return True if it does, and False if it does not.
    The function should accept three parameters: the first is the number, the second is the lowest value
    of the range, and the third is the highest value of the range.
2.  Write a function called find_evens that will accept a list of numbers as a parameter.
    The function should loop through the list and determine if each number is even. If it is, add it to a new list
    of only even numbers. Return the list of even numbers.
3.  Write a function called is_palindrome that will accept a string and return True if it is a palindrome,
    and False if it is not.
"""
def in_range (num, left, right):
    return left<num<right
"""
def is_palindrome(a):
    return a==a[::-1]
"""
def is_palindrome(a):
    for i in range(len(a)//2):
        if a[i] !=a[len(a)-i-1]:
            return False
    return True





racecar
"""
If you're finished, look up and read about what default parameters are. Then try one of the following function
challenges with default parameters:

1.  Write a function called greet_me that requires a name as a parameter, and has an optional greeting as a parameter.
    If a greeting is not passed, the function will greet the person with Hello. If a greeting is passed, it
    will use that greeting instead.
2.  Write your own function using a good use case for default parameters :)
"""
