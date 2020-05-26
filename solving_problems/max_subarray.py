def kadane_algo(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)-1):
        max_current = max(arr[i], max_current+arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


array = [-2, 3, 2, -1]
print(kadane_algo(array))
