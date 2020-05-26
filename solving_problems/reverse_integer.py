"""
The number 2,147,483,647 (or hexadecimal 7FFFFFFF16) is
the maximum positive value for a 32-bit signed binary integer in computing.
It is therefore the maximum value for variables declared as integers
in many programming languages, and the maximum possible score, money, etc.
for many video games. The appearance of the number often reflects an error,
overflow condition, or missing value.
The data type time_t, used on operating systems such as Unix,
is a signed integer counting the number of seconds since the start of
the Unix epoch (midnight UTC of 1 January 1970), and is often
implemented as a 32-bit integer.[11] The latest time that can be
represented in this form is 03:14:07 UTC on Tuesday, 19 January 2038
(corresponding to 2,147,483,647 seconds since the start of the epoch).
This means that systems using a 32-bit time_t type are susceptible
to the Year 2038 problem.[12]"""

# Problem: Given a 32-bit signed integer, reverse digits of an integer.
"""
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:

Assume we are dealing with an environment which could only store integers within
 the 32-bit signed integer range:
[−2^31, 2^31 − 1]. For the purpose of this problem,
!!!assume that your function returns 0 when the reversed!!!
integer overflows.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.

//pop operation:
pop = x % 10;
x //= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;

Luckily, it is easy to check beforehand whether or this statement would cause an overflow.
To explain, lets assume that 'rev' is positive.

If temp = rev * 10 + pop causes overflow, then it must be that rev >= INTMAX/10
If rev > INTMAX/10, then temp = rev * 10 + pop is guaranteed to overflow.
If rev == INTMAX/10, then then temp = rev * 10 + pop will overflow if and only if pop >7
Similar logic can be applied when 'rev' is negative and pop < -8.
"""

# Approach 1:


def reverse(x):
    absNum = abs(x)
    reversed = 0
    maxval = (2**31-1)
    minval = (2**31)
    while (absNum != 0):
        pop = absNum % 10
        reversed = reversed * 10 + pop
        absNum //= 10
    if (x > 0 and reversed < maxval):
        return reversed
    elif (x < 0 and reversed < minval):
        # less than min value (instead of more than it) bcs it is still abs value of reversed
        return -reversed
    else:
        return 'not a 32-bit integer'


print(reverse(-2**31))
# reversed version of 32-bit integer -2147483647 will be -7463847412,
# thus less than min 32-bit integer and should return 0
print(reverse(-7463847411))
# reversed version of the integer -7463847411 will be -1147483647,
# thus more than min 32-bit integer (-2147483647)
print(reverse(7463847412))
# reversed version of the integer 7463847412 will be 2147483647,
# thus equal to the 32-bit integer limit (2147483647)
print(reverse(-123))
# should return -321
print(reverse(120))
# should return 21


"""
Complexity Analysis:
Time Complexity: O(log(x)).
Space Complexity: O(1).
"""

# Approach 2: convert number to a string, save the sign of a number,
# revert the string and then concatenate with the sign and convert
# to number again


def reverse2(x):
    if x >= 2**31-1 or x <= -2**31:
        return 0
    else:
        strg = str(x)
        if x >= 0:
            revst = strg[::-1]
        else:
            temp = strg[1:]
            temp2 = temp[::-1]
            revst = "-" + temp2
        if int(revst) >= 2**31-1 or int(revst) <= -2**31:
            return 'not a 32-bit integer'
        else:
            return int(revst)


print(reverse2(-123))
print(reverse2((2**31-4)))
# reversed version of 32-bit integer 2147483647 will be 7463847412,
# thus more than max 32-bit integer and should return 0
