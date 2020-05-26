# very applicable in data security

"""
Non-repeating element
Take a string and return character that never repeats
if multiple uniques then return only the first unique
"""

# Solution 1 (O(n)):


def non_repeating(string):
    string = string.replace(" ", "").lower()
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    all_uniques = []
    for item in char_count.items():
        if item[1] == 1:
            all_uniques.append(item)
    return all_uniques


print(non_repeating("I apple Ape Peels"))
