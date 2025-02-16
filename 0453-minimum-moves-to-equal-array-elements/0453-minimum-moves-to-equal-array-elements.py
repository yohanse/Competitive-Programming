class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        ops = 0
        for i in range(1, len(nums)):
            turn = nums[i - 1] - nums[i]
            ops += turn*i
        return ops
