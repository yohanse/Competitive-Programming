class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 3)]

        for i in range(n):
            dp[i + 3] = min(dp[i], dp[i + 1], dp[i + 2]) + max(0, k - nums[i])
        
        return min(dp[-3:])