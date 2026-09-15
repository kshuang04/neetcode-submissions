class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        max_profit = 0
        l = 0
        for r in range(1, len(prices)):
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)
            if prices[r] <= prices[l]:
                l = r
        
        return max_profit
