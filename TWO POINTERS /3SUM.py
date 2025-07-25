# https://leetcode.com/problems/3sum/
# TLE - brute force 
class Solution(object):
    def threeSum(self, nums):
        result = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        return list(result)
