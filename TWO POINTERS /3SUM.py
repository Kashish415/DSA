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
# ---------------------------------------------------------------------------------------------
# optimized approach:
class Solution(object):
    def threeSum(self, nums):
        # Step 1: Sort the input list
        nums.sort()
        triplets = []

        # Step 2: Loop through the array
        for i in range(len(nums)):
            # Skip duplicate 'i' values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Use two pointers to find the remaining pair
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a valid triplet
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inward and skip duplicates
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1  # Need a bigger number
                else:
                    right -= 1  # Need a smaller number

        return triplets


