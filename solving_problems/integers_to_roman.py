# 13. Roman to Integer
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. The number twenty seven is written 
as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies
to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# Approach 1:


class Solution(object):
    def romanToInt(self, romChar):
        if not romChar:
            return 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        l = len(romChar)
        integer = dic[romChar[l-1]]
        # looping backwords from the end of roman characters and looking up corrwesponding
        # roman numerials in the dic:
        for i in range(l-1, 0, -1):
            current = dic[romChar[i]]
            prev = dic[romChar[i-1]]
            integer += prev if prev >= current else -prev
            # although roman figures are represented by putting characters in left-to-right order,
            # adding them up together, but as soon as number component should be less than
            # the possible closest maximum representation component,
            # it is split onto two characters:
            # the smaller one character is placed before the closest max component in a way
            # so that the component could be reduced by the smaller value on its left side.
            # Thus if previous integer value of the roman numeral in
            # our backward sequense (from right-to-left) is more than the current one
            # then add it up, otherwise substract
        return integer


rom_to_arab = Solution()
print(rom_to_arab.romanToInt('MMMCMLXXXVI'))
print(rom_to_arab.romanToInt('MMMM'))
print(rom_to_arab.romanToInt('C'))

"""
Complexity Analysis:
Time Complexity: O(n).
Space Complexity: O(1).
"""

# Approach 2: almost the same except the order of looping is different


class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                print(rom_val[s[i]] - 2 * rom_val[s[i - 1]])
                # since the previous character value of roman numeral have been already added up
                # and now it was figured out that the current character value is more than the previous
                # the previous one should be substracted twice
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val


"""
Complexity Analysis:
Time Complexity: O(n).
Space Complexity: O(1).
"""


print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))


"""
Problem: Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
Solution: The basic idea to convert roman to integer are
Sum same numbers (e.g. III = 3)
When next number is smaller than current one, add them (e.g. VI = 6)
When next number is larger than current one, use larger number — smaller number (e.g. IV = 4)
So for a case like XXIX, we loop through from beginning to the end. When next number is smaller
or equal to current number, sum them. When next number is larger than current number, 
sum them and minus twice of current number. The answer for XXIX is 10 + 10 + 1 + 10–2 * 1 = 29. 
Or we could loop from the end to forward. When previous number is smaller than current number, 
minus previous number. Otherwise, add them together. We have 10–1 + 10 + 10 = 29.
"""
