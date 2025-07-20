# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# https://leetcode.com/problems/missing-number/description

# Approach 1 
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()                # sort has n logn complexity

        for index, value in enumerate(nums):
            if (index != value):
                return index
            if value == (len(nums) - 1):
                return index + 1

# Approach 2 
# difference of the expected sum and the actual sum of the list gives the missing number 
# complexity: O(n)
class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums) # expected sum - actual sum 
