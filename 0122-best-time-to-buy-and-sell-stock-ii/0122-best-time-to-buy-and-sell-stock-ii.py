class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        sell = profit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            if sell > prices[i]:
                profit += sell - buy
                buy = prices[i]
                sell = 0
            elif buy > prices[i]:
                buy = prices[i]
            else:
                sell = prices[i]
        return profit + max(0, sell - buy)
            