# https://leetcode.com/problems/squares-of-a-sorted-array/

# approach 1
class Solution(object):
    def sortedSquares(self, nums):

        sq_list = [num ** 2 for num in nums]    # O(N)
        sq_list.sort()                        # O(N LOG N)

        return sq_list
# ----------------------------------------------------------------
# approach 2  ( double ended queue)
class Solution(object):
    def sortedSquares(self, nums):
        answer = collections.deque()
        left_ptr , right_ptr = 0, len(nums)-1
        
        while left_ptr <= right_ptr:
            left_value , right_value = abs(nums[left_ptr]), abs(nums[right_ptr])
            if left_value > right_value:
                answer.appendleft(left_value * left_value)
                left_ptr +=1
            else:
                answer.appendleft(right_value * right_value)
                right_ptr -= 1

        return list(answer)

    
        
        
