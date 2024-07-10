class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        GCD = gcd(*numsDivide)
        nums.sort()
        for i in range(len(nums)):
            if GCD % nums[i] == 0:
                return i
        return -1
        