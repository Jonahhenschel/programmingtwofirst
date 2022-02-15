



"""
Problem 0:
Choose at least three things from lessons that other classmates taught and incorporate them into a function that has
at least one parameter that is a list, and that returns something meaningful.
"""


"""
Problem 1:
Write a function called unique_append that will take in a list and an element to append as parameters.
If the element to append does not already exist in the list, it should append it to the list and return True.
If the element does exist in the list, it should not append it and return False. 
"""
def u_append(a,elm):
    if elm not in a:
        a.append(elm)
        return True
    else:
        return False
b=[1,2,3,4]
print(u_append(b,2))
print (b)
"""
Problem 2:
Write a function called find_max that takes in a list as a parameter and returns the maximum value in the list.
Sorry.... but you're not allowed to use the max function.
"""
def find_max(a):
    minimum=0
    for i in a:
        if i>minimum:
            minimum=i
    return minimum
print (find_max([1,2,3,4]))




"""
Problem 3:
Write a function called get_item that takes in a list and a (positive) index number as parameters. If the index number 
is not out of range for the given list, return the list item at that index. Otherwise, return None. 
"""
def get_item(a,num):
    if num<len(a):
        return a[num]
    else:
        return None
print (get_item([1,2,3,4],0))


"""
Problem 4:
Write a function called list_overlap that takes in two lists as parameters. This function should return a list that 
contains all the list items that exist in both of the lists passed in. 
P.S. You shouldn't use any built in functions for this.
"""


"""
Problem 5:
Write a function called index_wise_sum that takes in two lists (of the same length) as parameters. This function 
should return a new list (also of the same length) where each element is the result of the sum of the elements at that
same position in the two lists that were passed as parameters. For example, if the two lists passed in were
[1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] then the list returned would be [7, 9, 11, 13, 15]. You can choose how your 
function should behave if the lists passed in are not the same length.
"""