"""
Given 2 arrays (assume no duplicates)
is 1 array a rotation of another - return True/False
same size amd elements but start index is different

BigO(n) we are going through each array 2X but O(2n) = O(n)

Select an indexed position in list1 and gets its value. 
Find same element in list2 and check index for index from there
If any variation then we know it's false.
Getting to the last item without a false means true
"""


def rotation(list1, list2):
    if(len(list1) != len(list2)):
        return False

    key = list1[0]
    key_index = 0

    for i in range(len(list1)):
        if(list2[i] == key):
            key_index = i  # as soon as we encounter the same key value
            # in the second list we save its index to start looping through
            # the 1st list to check if values are the same and in the same
            # sequence but just starting point is rotated
            break
    if key_index == 0:
        return False

    for x in range(len(list1)):
        # start comparing each value from the beginning in
        # the 1st list with each value following the found
        # one at the first point in the second list

        # therefore loop through the 1st list while adding "x"
        # as a step to the found index of the value in
        # the 2nd list (taking into the account the initial shift)

        # use the modulo so that not to fall out of the list2 range,
        # given the initial shift, and while the iteration in the 1st
        # list has not been done yet
        """for instance we have these two lists:
        list1 = [1, 2, 3, 4, 5, 6, 7]
        list2 = [4, 5, 6, 7, 1, 2, 3]
        """
        # So at some point modulo will return the indices
        # which are less that that one where we started due to the shift
        # registered by key_index (4); thus we can check leftside values
        # in the second list

        l2index = (key_index + x) % len(list1)
        if list1[x] != list2[l2index]:
            return False
    return True


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 7, 1, 2, 3]
list3 = [1, 2, 3, 4, 5, 6, 7]
list4 = [4, 5, 7, 6, 1, 2, 3]
list5 = [1, 2, 3, 4]
list6 = [1, 2, 3, 4]
print(rotation(list1, list2))
print(rotation(list3, list4))
print(rotation(list5, list6))
