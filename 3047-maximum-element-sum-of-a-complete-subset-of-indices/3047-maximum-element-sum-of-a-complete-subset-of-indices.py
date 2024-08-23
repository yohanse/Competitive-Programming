class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumi = {}
        for i in range(1, len(nums) + 1):
            for k in range(1, 101):
                square = k*k
                quotient = i // square
                if i % square == 0:
                    sumi[quotient] = sumi.get(quotient, 0) + nums[i - 1]
        return max(sumi.values())