"""
Merge sort (also commonly spelled mergesort) is an O(n log n)
comparison-based sorting algorithm. Most implementations produce a stable sort,
which means that the implementation preserves the input order 
of equal elements in the sorted output.
"""

""" Sequence of merge sorting:
[21, 4, 1, 3, 9, 20, 25] (Original Array)
[21], [1, 4], [3, 9], [20, 25] (1)
[1,4,21], [3, 9, 20, 25] (2)
[1, 3, 4, 9, 20, 21, 25] (3)
"""


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call until we dip down to a main list of two elements, and when we split it in two halves, left and right,
        # with one element on each side, to compare them both and return them in their ordered positions to
        # the main list of two elements. After that, recursive calls return their main lists upward as the ordered
        # left and right sides, comparing them and putting in the main longer list, implementing the proce of merging gradually
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # the smaller wins, thus
                # The value from the left half has been used and put in the main list
                myList[k] = left[i]
                # Move the iterator in the left side forward
                i += 1
            else:
                # if not and an element from the right half is smaller then it takes place in the main list
                myList[k] = right[j]
                # Move the iterator in the right side forward
                j += 1
            # Move to the next slot in the main list
            k += 1

        # We check for the remaining element either in the left side or in the right side,
        # looking at the current indices of i and j, and put that element into the main list at the k position
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)
