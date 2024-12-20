class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[inf for i in range(m + 2)] for j in range(n + 1)]
        dp[0][0] = 0

        for i in range(n):
            for j in range(m + 1):
                maxi = sumi = count = 0
                for k in range(i, -1, -1):

                    maxi = max(maxi, nums[k])
                    sumi += nums[k]
                    count += 1
                    
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[k][j] + maxi*count - sumi)
        return dp[-1][-1]
