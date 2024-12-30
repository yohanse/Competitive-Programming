class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0 for i in range(k)] for j in range(n + 1)]
        sumi = count = 0
        for j in range(n):
            sumi += nums[j]
            count += 1
            dp[j + 1][0] = sumi/count
        
        for i in range(1, n):
            for j in range(1, k):
                sumi = count = 0
                for m in range(i, -1, -1):

                    sumi += nums[m]
                    count += 1

                    dp[i + 1][j] = max(dp[i + 1][j], dp[m][j - 1] + (sumi/count))
        return dp[-1][-1]