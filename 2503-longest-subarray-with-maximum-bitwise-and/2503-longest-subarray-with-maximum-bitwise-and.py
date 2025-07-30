class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = result = 0
        maxi = max(nums)
        for num in nums:
            if num == maxi:
                count += 1
            else:
                count = 0
            
            result = max(result, count)
        return result


        