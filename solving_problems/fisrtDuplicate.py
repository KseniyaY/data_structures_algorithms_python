# Problem: find the first (closest) occured duplicate in an array
# where integers are within a range from 1 to
# an integer equals to the length of the array itself
# (which is a subtle prompt to a solution):
# [2, 1, 3, 5, 3, 2]

array = [2, 1, 3, 5, 3, 2]

# O(n^2) The worst but most obvious case


def firstDuplicateWorst(arr):
    min_second_index = len(arr)
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                min_second_index = min(min_second_index, j)
    if(min_second_index == len(arr)):
        return -1
    else:
        return arr[min_second_index]


# O(n) better solution but with additonal space allocation
def firstDuplicateModerate(arr):
    seen = set()

    for i in range(0, len(arr)):
        if(arr[i] in seen):  # average case is O(1), worst case - O(n)
            return arr[i]
        else:
            seen.add(arr[i])
    return -1


# only if the range of integers is between 1 and the highest integer equals
# to the length of the given arr, and you are allowed to mutate array,
# then BEST solution is following:
# O(n) solution but without additional space allocation
def firstDuplicateBest(arr):
    for i in range(0, len(arr)):
        if(arr[abs(arr[i])-1] < 0):  # it means that we have already marked this element as negative,
            # so we've seen it before
            return abs(arr[i])
        else:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i])-1]
    return -1


# should return 3 in all calls
print(firstDuplicateWorst(array))
print(firstDuplicateModerate(array))
print(firstDuplicateBest(array))
