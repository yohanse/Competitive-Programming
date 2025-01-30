class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        number = 2**len(nums1) - 1
        dp = [[-1 for i in range(len(nums1))]for j in range(number + 1)]
        def rec(used1, index):
            if index == len(nums1):
                return 0

            if dp[used1][index] != -1:
                return dp[used1][index]

            dp[used1][index] = inf
            
            for i in range(len(nums1)):
                if used1 & (1 << i) == 0:
                    dp[used1][index] = min(dp[used1][index], rec(used1 | (1 << i), index + 1) + (nums1[index]^nums2[i]))
            return dp[used1][index]
        return rec(0, 0)
        