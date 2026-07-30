class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        profit = []

        for i in range(len(prices)):
            curr_max = 0
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > curr_max:
                    curr_max = prices[j] - prices[i]
            
            profit.append(curr_max)
        
        for p in profit:
            if p > max_profit:
                max_profit = p

        return max_profit