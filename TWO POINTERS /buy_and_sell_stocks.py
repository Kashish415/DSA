# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1709777934/

class Solution(object):
    def maxProfit(self, prices):
        left_ptr, right_ptr = 0,1   # initialise left & right pointer
        max_profit = 0

        while right_ptr != len(prices):
            if prices[left_ptr] < prices[right_ptr]:
                profit = prices[right_ptr] - prices[left_ptr]
                max_profit = max(max_profit, profit)    # update 

            else:
                left_ptr = right_ptr
            right_ptr += 1
        return max_profit
        
