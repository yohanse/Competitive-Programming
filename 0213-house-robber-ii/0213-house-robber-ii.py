class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_bank(nums):
            previous = pre_previous = 0
            for i in range(len(nums)):
                previous, pre_previous = max(previous, pre_previous + nums[i]), previous
            return max(previous, pre_previous)
        return max(rob_bank(nums[:-1]), rob_bank(nums[1:]))