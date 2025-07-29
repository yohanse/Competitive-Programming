class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        alternate = 1
        expect = 1 - nums[0]%2
        odd = nums[0] % 2
        even = 1 - nums[0]%2

        for i in range(1, len(nums)):
            if expect == nums[i]%2:
                expect = 1 - expect
                alternate += 1
            
            if nums[i]%2:
                odd += 1
            else:
                even += 1
        return max(even, odd, alternate)

        