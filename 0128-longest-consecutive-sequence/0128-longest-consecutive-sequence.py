class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in dic:
                length = 0
                while num + length in dic:
                    length += 1
                res = max(length, res)
        return res
