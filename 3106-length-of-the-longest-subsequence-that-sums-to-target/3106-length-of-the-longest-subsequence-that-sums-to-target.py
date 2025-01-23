class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
        dp[n] = [-inf for i in range(target + 1)]
        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for j in range(target + 1):
                dp[i][j] = dp[i + 1][j]
                if j - nums[i] > -1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - nums[i]] + 1)
                    
        if dp[0][target] == -inf:
            return -1
        return dp[0][target]