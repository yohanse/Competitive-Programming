class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[inf for i in range(m + 1)] for j in range(n + 1)]
        ans = -inf
        for i in range(n):
            for j in range(m):
                ans = max(ans, grid[i][j] - min(dp[i + 1][j], dp[i][j + 1]))
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], grid[i][j])
        
        return ans