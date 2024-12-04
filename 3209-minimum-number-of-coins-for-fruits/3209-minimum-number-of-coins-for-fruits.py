class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # memo = {}
        # def rec(index, free):
        #     if index == n:
        #         return 0

        #     if (index, free) in memo:
        #         return memo[(index, free)]

        #     memo[(index, free)] = rec(index + 1, 2*(index + 1)) + prices[index]
        #     if index < free:
        #         memo[(index, free)] = min(rec(index + 1, free), memo[(index, free)])
        #     return memo[(index, free)]
            
        # return rec(0, -1)

        dp = [[0 for i in range(n)] for j in range(n + 1)]
        
        for index in range(n - 1, -1, -1):
            for free in range(n - 1, -1, -1):
                dp[index][free] = prices[index]
                if 2*(index + 1) < n:
                    dp[index][free] += dp[index + 1][2*(index + 1)]

                if index < free:
                    dp[index][free] = min(dp[index][free], dp[index + 1][free])
        return dp[0][0]