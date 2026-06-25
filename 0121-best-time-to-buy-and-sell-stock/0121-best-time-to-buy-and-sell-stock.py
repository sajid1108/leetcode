class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Step 1: Initialize variables
        running_min = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < running_min:
                running_min = price
                
            if price - running_min > max_profit:
                max_profit = price - running_min
                
        return max_profit