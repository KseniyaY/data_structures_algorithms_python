"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Approach 1: Brute Force
# The brute force approach is simple. Loop through each element x
# and find if there is another value that equals to target - x.


def twoSum1(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[j] == target - nums[i]):
                return [i, j]
    print("There is no pair")


arr = [11, 7, 2, 15]
target = 18
print('First approach', twoSum1(arr, target))  # should return [1,2]

"""
Complexity Analysis
Time complexity : O(n^2). For each element, we try to find its complement
by looping through the rest of array which takes O(n) time.
Therefore, the time complexity is O(n^2).
Space complexity : O(1)."""


def twoSum2(nums, target):
    hashMap = {}
    for i in range(0, len(nums)):
        hashMap[nums[i]] = i
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if(complement in hashMap and hashMap[complement] != i):
            return [i, hashMap.get(complement)]
    print("There is no pair")


arr2 = [11, 7, 2, 15]
target2 = 18
print('Second approach', twoSum2(arr2, target2))  # should return [1,2]

# Approach 3
# It turns out we can do it in one-pass. While we iterate and
# inserting elements into the table, we also look back to check
# if current element's complement already exists in the table.
# If it exists, we have found a solution and return immediately.


def twoSum3(nums, target):
    hashMap = {}
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if(complement in hashMap):
            return [hashMap[complement], i]
        hashMap.update({nums[i]: i})
    # print("There is no pair")


arr3 = [11, 7, 2, 15]
target3 = 18
print('Third approach', twoSum3(arr3, target3))  # should return [1,2]


"""
Complexity Analysis:
Time complexity: O(n).
We traverse the list containing n elements only once.
Each look up in the table costs only O(1) time.
Space complexity: O(n). The extra space required
depends on the number of items stored in the hash table,
which stores at most nn elements."""
