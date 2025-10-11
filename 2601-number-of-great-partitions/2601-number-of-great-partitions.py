class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0 for _ in range(k)] for _ in range(n + 1)]
        dp[n] = [1 for _ in range(k)]

        for r in range(n - 1, -1, -1):
            for curr_sum in range(k - 1, -1, -1):
                dp[r][curr_sum] = dp[r + 1][curr_sum]
                if curr_sum + nums[r] < k:
                    dp[r][curr_sum] += dp[r + 1][curr_sum + nums[r]]
        
        # Number of subsets which have less than sum of k.
        subsets = dp[0][0]
        modulo = 10**9 + 7
        result = 2**n - 2*subsets
        
        return result%modulo if result > 0 else 0
