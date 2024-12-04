class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def rec(index, free):
            if index == n:
                return 0

            if (index, free) in memo:
                return memo[(index, free)]

            memo[(index, free)] = rec(index + 1, 2*(index + 1)) + prices[index]
            if index < free:
                memo[(index, free)] = min(rec(index + 1, free), memo[(index, free)])
            return memo[(index, free)]
            
        return rec(0, -1)