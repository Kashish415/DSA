# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array

class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}   # In python hashmap is a dictionary 

        for index, value in enumerate(nums):
            diff = target - value
            if diff in hash_map:
                return index , hash_map[diff]
            hash_map[value] = index
