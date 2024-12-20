class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[inf for i in range(k + 2)] for j in range(n + 1)]
        dp[0][0] = 0

        for i in range(n):
            for j in range(k + 1):
                maxi = sumi = count = 0
                for m in range(i, -1, -1):

                    maxi = max(maxi, nums[m])
                    sumi += nums[m]
                    count += 1

                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[m][j] + maxi*count - sumi)
        return dp[-1][-1]
