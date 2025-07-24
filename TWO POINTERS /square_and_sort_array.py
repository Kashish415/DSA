# https://leetcode.com/problems/squares-of-a-sorted-array/

# approach 1
class Solution(object):
    def sortedSquares(self, nums):

        sq_list = [num ** 2 for num in nums]
        sq_list.sort()

        return sq_list
    
        
