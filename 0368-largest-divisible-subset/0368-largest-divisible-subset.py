class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[1, i] for i in range(n)]
        nums.sort()
        answer = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i][0] < dp[j][0] + 1:
                    dp[i] = [dp[j][0] + 1, j]
                    if dp[answer][0] < dp[i][0]:
                        answer = i

        subset = []
        while dp[answer][1] != answer:
            subset.append(nums[answer])
            answer = dp[answer][1]
        subset.append(nums[answer])
        return subset
        
                
        