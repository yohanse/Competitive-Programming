class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)

        smallest_leng = len(nums) + 1
        for i in range(len(nums)):
            gcd_cal = nums[i]
            for j in range(i, len(nums)):
                gcd_cal = gcd(gcd_cal, nums[j])
                if gcd_cal == 1:
                    smallest_leng = min(smallest_leng, j - i + 1)
                    break
       
        if smallest_leng == len(nums) + 1:
            return -1
        return smallest_leng + len(nums) - 2
        