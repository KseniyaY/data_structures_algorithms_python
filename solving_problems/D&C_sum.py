# Divide and Conquer implementation

arr = [1, 2, 3, 4, 5]  # find the sum
arr2 = [1, 7, 3, 4, 5]  # find the max


def getSumRecursively(arr):
    if not arr:  # edge case/negative case
        return
    if len(arr) == 1:  # base case
        return arr[0]
    else:
        return arr[0] + getSumRecursively(arr[1:])  # recursive case


print(getSumRecursively(arr))


def getMax(arr):
    if not arr:  # edge case/negative case
        return
    elif len(arr) == 1:  # base case
        return arr[0]
    else:
        return max(arr[0], getMax(arr[1:]))  # recursive case


print(getMax(arr2))
