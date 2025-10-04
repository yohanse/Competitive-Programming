class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [0 for _ in range(max(n + 1, 11))]
        dp[2] = dp[5] = dp[6] = dp[9] = 1
        dp[4] = dp[7] = dp[3] = -1
        count = 0
        for num in range(1, n + 1):
            quotient, reminder = num // 10, num%10

            if dp[quotient] == -1 or dp[reminder] == -1:
                dp[num] = -1
            
            elif dp[quotient] == 1 or dp[reminder] == 1:
                dp[num] = 1
                count += 1
            else:
                dp[num] = 0
            

        return count