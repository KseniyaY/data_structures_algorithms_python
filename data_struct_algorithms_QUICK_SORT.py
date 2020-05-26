
"""
Quicksort is a comparison sort, meaning that it can sort items of any type
for which a "less-than" relation (formally, a total order) is defined. 
Inefficient implementations it is not a stable sort, meaning that
the relative order of equal sort items is not preserved. Quicksort can operate
in-place on an array, requiring small additional amounts of memory to perform the sorting.
"""

# # Quicksort is recursive and Divide-and-Conquer algorithms
# # worst case is O(n^2)
# # average and best case is O(n log n)

# Solution 1


def quicksort_recursive(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)


print(quicksort_recursive([10, 5, 2, 3]))

# Solution 2
passes_recursively = 1
# # we initialize with 1 at once, since the first call of function is a first interation
# # and before another recursive call each time will be added 1

# quicksort with the pivot at a median position


def quick_sort(arr):
    lowIdx = 0
    highIdx = len(arr)-1
    quick_sort_recursive(arr, lowIdx, highIdx)


def quick_sort_recursive(arr, lowIdx, highIdx):
    global passes_recursively
    if highIdx - lowIdx < len(arr) and lowIdx < highIdx:
        quick_selection(arr, lowIdx, highIdx)
    if lowIdx < highIdx:  # if there is more than 1 element to be sorted
        pivot = partition(arr, lowIdx, highIdx)
        quick_sort_recursive(arr, lowIdx, pivot-1)
        passes_recursively += 1
        # quick_sort_recursive(arr, lowIdx, pivot)
        quick_sort_recursive(arr, pivot+1, highIdx)
        passes_recursively += 1


def partition(arr, lowIdx, highIdx):
    pivotIdx = get_pivot(arr, lowIdx, highIdx)
    pivotVal = arr[pivotIdx]
    arr[pivotIdx], arr[lowIdx] = arr[lowIdx], arr[pivotIdx]
    border = lowIdx

    for i in range(lowIdx, highIdx + 1):
        if arr[i] < pivotVal:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[lowIdx], arr[border] = arr[border], arr[lowIdx]

    return (border)


def get_pivot(arr, lowIdx, highIdx):
    midIdx = (lowIdx + highIdx) // 2
    s = sorted([arr[lowIdx], arr[midIdx], arr[highIdx]])
    if s[1] == arr[lowIdx]:
        return lowIdx
    elif s[1] == arr[midIdx]:
        return midIdx
    return highIdx


def quick_selection(arr, first, last):
    for i in range(first, last):
        minIdx = i
        for j in range(i+1, last+1):
            if arr[j] < arr[minIdx]:
                minIdx = j
        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]


arr_to_be_sorted_1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
length = len(arr_to_be_sorted_1)
quick_sort(arr_to_be_sorted_1)
print('recursively sorted with a median pivot: ', arr_to_be_sorted_1)
print('recursively passed #1', passes_recursively)

# quicksort with the pivot at the last (right) position

# Solution 3
passes_recursively_2 = 1


def quicksort_2(arr):
    quicksort_recursion(arr, 0, len(arr)-1)
    return arr


"""
Top level function that calls 'partition' and splits the data based on where
'partition' leaves the choosen pivot value
"""


def quicksort_recursion(arr, left, right):
    global passes_recursively_2
    # if an array is more than one element
    if(left < right):
        """Partition and sort the array from left to right and find where the selected pivot
        belongs"""
        pivotPosition = partition_2(arr, left, right)
        # Call quicksort_recursion to the left and to the right of the pivot
        quicksort_recursion(arr, left, pivotPosition - 1)
        passes_recursively_2 += 1
        quicksort_recursion(arr, pivotPosition + 1, right)
        passes_recursively_2 += 1


"""
The partition function that chooses a pivot, partitions the array around the
pivot, places the pivot value where it belongs, and then returns the index of
where the pivot finally lies
"""


def partition_2(arr, left, right):
    """
    In this implementation of quicksort we pick the last item in the partition
    space as the pivot everytime. This can turn out very good or very badly
    """
    if(left < right):
        pivot = arr[right]

        i = left-1  # so that we can be one step back to have "space" swapping
        # beetween the lesser than pivot number and bigger. In essence we push
        # the lesser element back behind the bigger
        """
        i will keep track of the "tail" of the section of items less than the pivot
        so that at the end we can "sandwich" the pivot between the section less than
        it and the section greater than it. 
        In essence, after being incremented certain number of times finally variable i will be
        the index position to swap the element at i position with the pivot from 
        the last/first index (depending on the approach)
        """

        """
        j will scan for us.
        """
        for j in range(left, right):
            """
            If this item is less than the pivot it needs to be moved to the section of
            items less than the pivot
            """
            if arr[j] <= pivot:
                """
                Move i forward so that we can swap the value at j into the tail of the items
                less than the pivot
                """
                i += 1
                """
                Execute the swap. We "throw" the item at j back into the section of items
                less than the pivot
                """
                print('i is', i)
                print('j is', j)
                print('elem at i is', arr[i])
                print('elem at j is', arr[j])
                arr[i], arr[j] = arr[j], arr[i]
        """
        Swap the pivot value RIGHT AFTER the section of items less than the pivot. i
        keeps the tail of this section. We shift 
        """
        arr[i+1], arr[right] = arr[right], arr[i+1]
        print('elem swapped with the pivot is', arr[i+1])
        print('the pivot is', arr[right])
        return i+1
        # Return the pivot's final resting position


array_to_sort = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print('recursively sorted with a pivot at the last right position:',
      quicksort_2(array_to_sort))
print('recursively passed #2', passes_recursively_2)
