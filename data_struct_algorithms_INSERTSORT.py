""" "Insertion sort is a simple sorting algorithm that builds
the final sorted array (or my_list) one item at a time. It is much
less efficient on large myLists than more advanced algorithms 
such as quicksort, heapsort, or merge sort."""


def insertionSort(my_list):
    # looping through each element, and tracking the current position with the index,
    # launch the comparison beetween previous values relying on the variable "position"
    # which can step back
    for index in range(1, len(my_list)):
        # we start from 1 since in case when a first element in a list is less than
        # the next one we need space to swap the values and put the smallest to the position -1,
        # e.g. to the index 0

        current_value = my_list[index]
        position = index

        # while current position is more than 0 and a value in a previous position is more than a current value,
        # swap them, => insert the previous value in the current position
        # Shift position one step back
        while position > 0 and my_list[position-1] > current_value:
            my_list[position] = my_list[position-1]
            position = position-1
        # assign the current value to the current position
        my_list[position] = current_value


my_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
insertionSort(my_list)
print(my_list)

"""the alternative slightly different way of """


def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Set key:
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            # Swap:
            arr[j + 1] = arr[j]
            arr[j] = key

            # Decrement 'j':
            j -= 1

    return arr


array = [5, 2, 12, 12, 1]
print("Original array: %s" % array)
print("Sorted array: %s" % insertion_sort(array))
