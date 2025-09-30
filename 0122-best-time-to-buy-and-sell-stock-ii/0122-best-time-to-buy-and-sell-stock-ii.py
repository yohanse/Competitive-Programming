class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[r - 1]:
                profit += prices[r - 1] - prices[l]
                l = r
        
        profit += prices[-1] - prices[l]
        return profit
        