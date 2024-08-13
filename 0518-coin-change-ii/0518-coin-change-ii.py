
            
        


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for i in range(n)] for j in range(amount + 1)]
        dp[0] = [1 for i in range(n)]

        for money in range(1, amount + 1):
            for index in range(n):
                dp[money][index] = dp[money][index - 1]
                if money - coins[index] >= 0:
                    dp[money][index] += dp[money - coins[index]][index]
       
        return dp[-1][-1] 