class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix_sum = {0:0}
        sumii = 0
        prev = 0
        for i in range(n):
            sumii += nums[i]
            diff = sumii - target
            prefix_sum[sumii] = max(prefix_sum.get(sumii, 0), prefix_sum.get(diff, -1) + 1, prev)
            prev = prefix_sum[sumii]
        return max(prefix_sum.values())