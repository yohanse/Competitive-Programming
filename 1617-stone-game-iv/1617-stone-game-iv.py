class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for i in range(n + 1)]
        

        for i in range(n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = dp[i] or (not dp[i - j**2])
        
        return dp[-1]