"""
given an arry what is the most frequently occurring element
"""


def most_frequent(list):
    count = {}
    max_count = 0
    most_freq_item = None

    for i in list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            most_freq_item = i
    return most_freq_item


print(most_frequent([1, 3, 3, -5, -5, -5, 3, 2, -5, 1, 1, 1, -5]))
