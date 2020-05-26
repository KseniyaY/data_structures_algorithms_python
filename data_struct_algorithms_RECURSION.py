"""Implement a function recursively to get the desired
Fibonacci sequence value.

fib_sequence = [0,1,1,2,3,5,8,13,21,34...n]
In essence,
fib_sequence[7] = 13
fib_sequence[9] = 34
fib_sequence[11] = 89
fib_sequence[0] = 0
So we should have a way to find a number in certain position,
knowing the principle of the sequence"""


def get_fib_recursive(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib_recursive(position-1)+get_fib_recursive(position-2)
    return -1


def get_fib_iterative(position):
    if position == 0:
        return 0
    if position == 1:
        return
    first = 0
    second = 1
    next = first + second
    i = 2
    while i < position:
        i += 1
        first = second
        second = next
        next = first + second
    return next


# Test cases
print(get_fib_recursive(7))  # fib_sequence[7] = 13
print(get_fib_recursive(9))  # fib_sequence[9] = 34
print(get_fib_recursive(11))  # fib_sequence[11] = 89
print(get_fib_recursive(0))  # fib_sequence[0] = 0

print(get_fib_iterative(7))  # fib_sequence[7] = 13
print(get_fib_iterative(9))  # fib_sequence[9] = 34
print(get_fib_iterative(11))  # fib_sequence[11] = 89
print(get_fib_iterative(0))  # fib_sequence[0] = 0
