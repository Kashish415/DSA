# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums):  
            return False
        else:
            return True
