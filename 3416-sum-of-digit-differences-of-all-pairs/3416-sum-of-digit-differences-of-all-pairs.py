class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        digits = [[0 for i in range(10)] for j in range(10)]
        ans = 0
        for i in range(len(nums)):
            index = 0
            while nums[i]:
                reminder = nums[i] % 10
                digits[index][reminder] += 1
                ans += sum(digits[index]) - digits[index][reminder]
                nums[i] //= 10
                index += 1
        return ans
        