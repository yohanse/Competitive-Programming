class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[i, i] for i in range(n + 2)]
        def modularize(x):
            return x % (10 ** 9 + 7)

        for i in range(3, n + 2):
            dp[i] = [modularize(sum(dp[i - 1])), 
                    modularize(2 * dp[i - 2][0] + dp[i - 2][1])]
        
        ans = sum(dp[-2])
        for i in range(n):
            ans = modularize(ans + modularize(max(sum(dp[i]), 1) * max(sum(dp[n - i - 1]), 1)))
        return ans