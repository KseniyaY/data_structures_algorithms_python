"""
Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
# Approach 1: O(n) two pointer solution


class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # we can do sort

        if(len(nums) == 0):
            return None

        current, start, end = 0, 0, len(nums)-1
        stepsCounter = 0

        while(current <= end):
            if nums[current] == 0:
                # if a value is "0" we keep it at the 'current' position before
                # the 'start' position, techically swapping 'start' and 'current';
                # bcs even if 'start' position contains "0" zero as well
                # such swap wouldn't hurt; in other cases (with 1 and 2) it will be exactly
                # what we intended to do - put zero before that 1 or 2
                nums[start], nums[current] = nums[current], nums[start]
                # move both pointers forward
                current += 1
                # as soon as we have zero at the start of the list we are
                # satisfied and can consider this part of a list sorted and start
                # the next step from the next element
                start += 1
                stepsCounter += 1
            elif(nums[current] == 2):
                # if there is a value of "2" that is obvious it should be at the third
                # section of a sorted list and therefore we place it at the end
                # meanwhile "current" pointer stays the same but the 'end' pointer
                # moves one step closer to the left/start of the list
                nums[end], nums[current] = nums[current], nums[end]
                end -= 1
                stepsCounter += 1
            else:
                # in case if "current" equals to "1", we just move the pointer
                # one step forward and on the next step of the cycle this "1"
                # will be compared as the "start" value and will be swapped if necessary
                # either before "current" or with the "end" pointer
                current += 1
                stepsCounter += 1
        print(stepsCounter)


dutchFlagProblem = Solution1()
toBeSorted = [2, 2, 1, 0, 2, 1, 0, 2, 0]
dutchFlagProblem.sortColors(toBeSorted)
print(toBeSorted)


# Approach 2: O(n) pivot partioning
class Solution2:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        stepsCounter = 0
        if not nums:
            return nums

        small, equal, large = 0, 0, len(nums)
        pivot = 1

        while equal < large:

            if nums[equal] < pivot:
                nums[small], nums[equal] = nums[equal], nums[small]
                small, equal = small + 1, equal + 1
                stepsCounter += 1

            elif nums[equal] == pivot:
                equal += 1
                stepsCounter += 1

            # nums[equal] > pivot
            else:
                large -= 1
                nums[equal], nums[large] = nums[large], nums[equal]
                stepsCounter += 1
        print(stepsCounter)
        return nums


dutchFlagProblem2 = Solution2()
toBeSorted2 = [2, 2, 1, 0, 2, 1, 0, 2, 0]
dutchFlagProblem2.sortColors(toBeSorted2)
print(toBeSorted2)
