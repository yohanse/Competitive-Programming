class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = "#"
        freq = 0

        for num in nums:
            if candidate != num:
                freq -= 1
                if freq < 0:
                    candidate = num
                    freq = 0
            else:
                freq += 1
        return candidate