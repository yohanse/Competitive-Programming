class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        def max_sum(nums):
            sumi = 0
            max_sum_v = -inf
            for num in nums:
                sumi += num
                max_sum_v = max(max_sum_v, sumi)
                sumi = max(sumi, 0)
                
            return max_sum_v


        return max(max_sum(nums), max_sum([-num for num in nums]))
        
        