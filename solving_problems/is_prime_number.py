"""
Check if a number is prime by checking for divisibility on numbers less than it.
Prime number is a number which is divided only by itself and 1.
It only needs to go up to the square root of 'n' (in the for loop),
because if 'n' is divisible by a number greater than its square root then
it's divisible by something smaller than it/
For example, while 33 is divisible by 11 (which is greater than the square root of 33),
the "counterpart" to 11 is 3 (3*11=33). 33 will have already been eliminated
as a prime number by 3
"""

# There are two solutions and each of them present O(√N)


import math


def isPrime(n):
    i = 2
    while i**2 <= n:  # the loop hits only to the point of the square root value of n
        if n % i == 0:
            return False
        i += 1
    return True


print(isPrime(33))
print(isPrime(27))
print(isPrime(11))


def isPrime2(n):
    i = 2
    # the loop hits only to the point of the square root value of n
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


print(isPrime2(33))
print(isPrime2(27))
print(isPrime2(11))
