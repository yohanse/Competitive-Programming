class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        remaining_sum = sum(nums) - x

        if remaining_sum < 0:
            return -1
        
        number_of_operation = len(nums) + 1
        curr_subarray_sum = 0

        l = 0
        for r in range(len(nums)):
            curr_subarray_sum += nums[r]
            while curr_subarray_sum > remaining_sum:
                curr_subarray_sum -= nums[l]
                l += 1
            
            if curr_subarray_sum == remaining_sum:
                number_of_operation = min(number_of_operation, len(nums) - (r - l + 1))
        
        if number_of_operation == len(nums) + 1:
            return -1
        
        return number_of_operation