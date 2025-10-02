class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Defining the state
            # index, color
        
        # Initilalize all valid states
            # index in [0, n]
            # color in [0, 2]

        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n + 1)]


        # state transition
            # i, c
            # dp[i][c] = min(dp[i + 1][c1], dp[i + 1][c2]) + costs[i][c]
        
        for index in range(n - 1, -1, -1):
            for color in range(3):
                dp[index][color] = min(dp[index + 1][(color + 1)%3], dp[index + 1][(color + 2)%3]) + costs[index][color]
        
        return min(dp[0])