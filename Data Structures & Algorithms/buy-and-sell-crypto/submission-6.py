class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        
        l = 0
        for r in range(len(prices)):
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)

            if prices[r] < prices[l]:
                l = r
        
        return max_profit