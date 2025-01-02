class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)
            
        smallest_leng = len(nums) + 1
        for i in range(len(nums)):
            for j in range(i):
                if gcd(*nums[j:i+1]) == 1:
                    smallest_leng = min(smallest_leng, i - j + 1)
       
        if smallest_leng == len(nums) + 1:
            return -1
        return smallest_leng + len(nums) - 2
        