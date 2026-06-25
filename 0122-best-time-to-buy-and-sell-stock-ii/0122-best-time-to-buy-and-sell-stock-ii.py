class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total_profit = 0

        for i in range(1,len(prices)):
            today = prices[i]
            yesterday = prices[i-1]
        
            if today > yesterday :
                total_profit += today - yesterday
            
        
        return total_profit


        