class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # Defining the state
            # index, color
        
        # Initilalize all valid states
            # index in [0, n]
            # color in [0, 2]

        n = len(costs)
        k = len(costs[0])
        dp = [[0 for _ in range(k)] for _ in range(n + 1)]


        # state transition
            # i, c
            # dp[i][c] = min(dp[i + 1][c1], dp[i + 1][c2]) + costs[i][c]
        
        for index in range(n - 1, -1, -1):
            for color in range(k):
                dp[index][color] = min([dp[index + 1][(color + c)%k] for c in range(1, k)]) + costs[index][color]
            print(dp[index])
        return min(dp[0])