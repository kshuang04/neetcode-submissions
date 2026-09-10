class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        profit = 0

        l = 0
        r = 1

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            profit = max(curr_profit, profit)

            if prices[r] < prices[l]:
                l = r
            
            r += 1
        
        return profit