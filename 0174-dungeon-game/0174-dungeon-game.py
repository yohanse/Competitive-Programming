class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])

        dp = [[-inf for i in range(m + 1)] for j in range(n + 1)]
        dp[-1][-2] = dp[-2][-1] = 0

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                dp[r][c] = min(0, max(dp[r + 1][c], dp[r][c + 1]) + dungeon[r][c])
        
        return max(1 - dp[0][0], 1)