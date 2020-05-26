"""
Write a function that reverses a string. The input string is given as
an array of characters char[].

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

# Approach 1 for fun :), but not applicable for other langs:
# Life is short, use Python. (c)


class Solution:
    def reverseString(self, s):
        s.reverse()

# or


"""This is a solution to reverse a word order"""


def reverse(s):
    return " ".join(s.split()[::-1])


print(reverse("This is the best"))


"""Speaking seriously, let's use this problem to discuss two things:
Does in-place mean constant space complexity?
Two pointers approach."""

# Approach 2:
"""Recursion, In-Place, O(n) space. Does in-place mean constant space complexity?
No. By definition, an in-place algorithm is an algorithm which transforms
input using no auxiliary data structure.
The tricky part is that space is used by many actors, not only by data structures.
The classical example is to use recursive function without any auxiliary data structures.
Is it in-place? Yes.
Is it constant space? No, because of recursion stack.

Here is an example. Let's implement recursive function helper which receives
two pointers, left and right, as arguments.
Base case: if left >= right, do nothing.
Otherwise, swap s[left] and s[right] and call helper(left + 1, right - 1).
To solve the problem, call helper function passing the head and tail indexes
 as arguments: return helper(0, len(s) - 1).
"""


class Solution2:
    def reverseString(self, s):
        # we can not deal with a string directly bcs it is immutable and
        # will throw an error as soon as we try to swap two characters
        s = list(s)

        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]

                helper(left + 1, right - 1)
        helper(0, len(s) - 1)
        s = "".join(s)
        return s


pyRecursSolution = Solution2()
print(pyRecursSolution.reverseString('hello!'))

# Approach 3:
# Approach 2: Two Pointers, Iteration, O(1) space (it is not in-place space complexity  after converting string to an array)
"""
In this approach, two pointers are used to process two array elements
at the same time. Usual implementation is to set one pointer in the beginning
and one at the end and then to move them until they both meet.
Sometimes one needs to generalize this approach in order to use three pointers,
like for classical Sort Colors problem.

Algorithm:
Set pointer left at index 0, and pointer right at index n - 1,
where n is a number of elements in the array.
While left < right:
Swap s[left] and s[right].
Move left pointer one step right, and right pointer one step left."""


class Solution3:
    def reverseString(self, s):
        # we can not deal with a string directly bcs it is immutable and
        # will throw an error as soon as we try to swap two characters
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        s = "".join(s)
        return s


pyIterSolution = Solution3()
print(pyIterSolution.reverseString('hello!'))


"""
Complexity Analysis
Time complexity: O(N) to swap N/2 element.

Space complexity: O(1), it's a constant space solution. (it is not in-place space complexity after converting string to an array)
"""

"""This is a solution to reverse a word order, including the letters' order"""


def reverse4(s):
    length = len(s)
    space = " "
    words = []
    i = 0
    while i < length:
        if s[i] != space:
            word_starts = i  # to track the start of the each word in a string

            while i < length and s[i] != space:
                # unless we encounter a new space we incement i
                # so that when it is a space finally we could define the range to cut
                # the current word from the string
                i += 1
            words.append(s[word_starts:i])
        # after the second inner cycle is done increment i one more time to go out from
        # the outer cycle
        i += 1
    # and return the new string by means of joining them in a reversed order
    return "".join(reversed(s))


print(reverse4("This is the best"))
