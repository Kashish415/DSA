# https://leetcode.com/problems/longest-mountain-in-array/
class Solution(object):
    def longestMountain(self, arr):
        # first and last items cannot be peaks so skip checking them
        result = 0

        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l=r=i
                while l>0 and arr[l] > arr[l-1]:
                    l -= 1
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r += 1
                result = max(result, r-l+1)
        return result 
