class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        two = five = 0
        dp = [[0, 0] for i in range(n + 1)]
        for i in range(1, n + 1):
            
            if i % 2 == 0:
                dp[i][0] = dp[i//2][0] + 1
                two += dp[i][0]
                
            if i % 5 == 0:
                dp[i][1] = dp[i//5][1] + 1
                five += dp[i][1]
        return min(two, five)