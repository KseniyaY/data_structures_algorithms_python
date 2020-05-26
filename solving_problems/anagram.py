"""
Given two strings, check to see if they are anagrams.
An anagram is when two strings can be written with the exact
same letters (so you can just reaarange the letters to get
a different phrase or word).
For example:
'dog' is anagram for 'god',
'public relations' is anagram for 'crap built on lies', ;)
Note: Ignore the spaces and capitalization.
"""

# Approach1 with built-in Python methods


def anagram(s1, s2):
    # remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Return boolean for sorted match
    return sorted(s1) == sorted(s2)


print(anagram('dog', 'god'))
print(anagram('public relations', 'crap built on lies'))
print(anagram('clint eastwood', 'old west action'))
print(anagram('aa', 'bb'))


# Approach 2
def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # check if same number of letters
    if len(s1) != len(s2):
        return False
    # count frequency of each letter
    count = {}
    for letter in s1:  # for every letter in first string
        if letter in count:  # if letter is already in my dictionary, then
            count[letter] += 1  # add 1 to that letter key
        else:
            count[letter] = 1  # if not just put 1

    # do reverse for second string
    for letter in s2:
        if letter in count:
            # substract 1 from a letter counter in the disctionary
            count[letter] -= 1
        else:
            count[letter] = 1  # otherwise just put 1

    for k in count:
        if count[k] != 0:  # as soon as there is a counter value
            # more than 1 for this letter given two words are not anagrams
            return False
    return True


print(anagram2('dog', 'god'))
print(anagram2('public relations', 'crap built on lies'))
print(anagram2('clint eastwood', 'old west action'))
print(anagram2('aa', 'bb'))
