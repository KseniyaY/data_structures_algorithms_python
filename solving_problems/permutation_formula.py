"""
if you want to know the number of ways (disregarding order) that k objects can be chosen
from among n objects; more formally, the number of k-element subsets (or k-combinations) 
of an n-element set, you can use the formula:
nCk = n!/(n-k)!/k! = n!/(k!(n-k)!)
"""
from math import factorial as fac


def binomial(n, k):
    try:
        binom = fac(n) // fac(k) // fac(n - k)
    except ValueError:
        binom = 0
    return binom


"""You just got a free ticket for a boat ride, and you can bring along 3 friends! 
Unfortunately, you have 5 friends who want to come along.
How many different groups of friends could you take with you?"""

print(binomial(5, 3))

"""
The rule of combinatorics is multiplication numbers of different available elements!
For instance, if you have 3 types of robot heads, 4 types of bodies and
7 types of arms, you can build 84 unique robots:
3*4*7=84 
What if you have to build robots with two different heads, then
you can use the following formula:
h*(h-1)*b*a or 3*2*4*7=168 different robots
(instead of previous 84 ones).
We use (h-1) bcs the second head variant has 1 less options
since that 1 has been already used by the first head"""
