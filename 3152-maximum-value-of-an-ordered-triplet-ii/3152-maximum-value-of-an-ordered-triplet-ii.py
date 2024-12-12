class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]

        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i])
            right[n - i - 1] = max(right[n - i], nums[n - i - 1])
        
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, (left[i - 1] - nums[i])*right[i + 1])
        return ans