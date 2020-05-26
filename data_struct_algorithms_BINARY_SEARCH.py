from collections import deque
"""
Binary Search : In computer science, a binary search or half-interval search algorithm
finds the position of a target value within a sorted array. The binary search algorithm
can be classified as a dichotomies divide-and-conquer search algorithm and executes in
logarithmic time.
"""


"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

# recursive binary search. Returns index if present else -1


def binary_search_recursive(input_array, value, first=0, last=0):
    # Your code goes here
    if not last:
        last = len(input_array) - 1
    mid = (last + first)//2
    if first <= last:
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            first = mid+1
        else:
            last = mid-1
        return binary_search_recursive(input_array, value, first, last)
    return -1


# Iterative binary search. Returns index if present else -1
def binary_search_iterative(input_array, value):
    # Your code goes here.
    first = 0
    last = len(input_array)-1
    found = None
    while(first <= last and not found):
        mid = (first + last)//2
        if input_array[mid] == value:
            return mid
        else:
            if value < input_array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_list_2 = [-11, -9, -3, -1, 15, 19, 29]
test_val = 15
test_val1 = 25
test_val3 = -9
print(binary_search_iterative(test_list, test_val))
print(binary_search_iterative(test_list, test_val1))
print(binary_search_iterative(test_list_2, test_val1))
print(binary_search_iterative(test_list_2, test_val3))
print(binary_search_recursive([1, 2, 3, 5, 8], 6))
print(binary_search_recursive([1, 2, 3, 5, 8], 5))
print(binary_search_recursive(test_list_2, test_val))
print(binary_search_recursive(test_list_2, test_val3))
