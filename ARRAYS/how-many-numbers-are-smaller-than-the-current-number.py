# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/?envType=problem-list-v2&envId=array

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        d = {}

        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i 

        return_list = []
        for i in nums:
            return_list.append(d[i])
        return return_list 
