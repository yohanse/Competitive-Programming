class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        res = nums.copy()
        N = len(nums)

        res[1] = max(res[0], res[1])
        for i in range(2, N - 1):
            res[i] = max(res[i - 2] + res[i], res[i - 1])
        
        nums[-2] = max(nums[-1], nums[-2])
        for i in range(N - 3, 0, -1):
            nums[i] = max(nums[i + 2] + nums[i], nums[i + 1])

        return max(max(res), max(nums))
        

        