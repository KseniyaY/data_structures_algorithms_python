"""
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm
that repeatedly steps through the list to be sorted, compares each pair of adjacent
items and swaps them if they are in the wrong order. The pass through the list is
repeated until no swaps are needed, which indicates that the list is sorted. The algorithm,
which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list.
Although the algorithm is simple, it is too slow and impractical for most problems even
when compared to insertion sort. It can be practical if the input is usually in sort order
but may occasionally have some out-of-order elements nearly in position.
"""

""" Sequence of bubble sorting:
[21, 4, 1, 3, 9, 20, 25, 6, 21, 14] (Original Array)
[4, 1, 3, 9, 20, 21, 6, 21, 14, 25] (1)
[1, 3, 4, 9, 20, 6, 21, 14, 21, 25] (2)
[1, 3, 4, 9, 6, 20, 14, 21, 21, 25] (3)
[1, 3, 4, 6, 9, 14, 20, 21, 21, 25] (4)
"""

# O(n ^ 2):
# the number of passes to sort + 1 for check that an array is actually completely sorted
passes_recursively = 1
# we initialize with 1 at once, since the first call of function is a first interation
# and before another recursive call each time will be added 1
passes_iteratively = 0


def bubble_sort_recursive(arr):
    swapped = 0
    global passes_recursively
    for index in range(len(arr)-1):
        if arr[index] > arr[index + 1]:
            arr[index + 1], arr[index] = arr[index], arr[index + 1]
            swapped += 1
    if swapped == 0:
        return arr
    else:
        passes_recursively += 1
        return bubble_sort_recursive(arr)


def bubble_sort_iterative(arr):
    global passes_iteratively
    passes_iteratively = 0
    for elem in range(len(arr)):
        swapped = 0
        index = 0
        passes_iteratively += 1
        while index < len(arr)-1:
            if(arr[index] > arr[index + 1]):
                arr[index + 1], arr[index] = arr[index], arr[index + 1]
                swapped += 1
            index += 1
        if(swapped == 0):
            break
    return arr


arr_to_be_sorted_1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
arr_to_be_sorted_2 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
sorted_recursively = bubble_sort_recursive(arr_to_be_sorted_1)
print('recursively sorted: ', sorted_recursively)
print(passes_recursively)

sorted_iteratively = bubble_sort_iterative(arr_to_be_sorted_2)
print('iteratively sorted: ', sorted_iteratively)
print(passes_iteratively)
