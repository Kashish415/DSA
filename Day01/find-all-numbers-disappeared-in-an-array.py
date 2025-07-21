# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=array

# We need to return the array of numbers that are missing from the range of 1 to n 
# where n =  length of the list  


class Solution(object):
    def findDisappearedNumbers(self, nums):
        set_nums = set(nums)
        missing = []

        for i in range(1, len(nums)+ 1):
            if i not in set_nums:
                missing.append(i)

        return missing 
