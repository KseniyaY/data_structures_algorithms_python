"""
Given a string, are all characters unique?
Should give a True or False return
Uses python built-in structures
"""
# Solution 1


def unique(string):
    string = string.replace(" ", "")
    return len(set(string)) == len(string)


print(unique("a b cdef"))


# Solution 2
def unique2(string):
    string = string.replace(" ", "")
    characters = set()

    for letter in string:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True


print(unique2("a b cdfef"))
