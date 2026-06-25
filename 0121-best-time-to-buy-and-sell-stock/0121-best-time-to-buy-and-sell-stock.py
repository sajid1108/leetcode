class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Step 1: Initialize variables
        running_min = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < running_min:
                running_min = price
                
            current_profit = price - running_min
            
        
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit