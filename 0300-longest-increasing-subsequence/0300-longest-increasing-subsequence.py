class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        leng = len(nums)
        dp = [1 for _ in range(leng)]
        for i in range(leng):
            for j in range(i + 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        