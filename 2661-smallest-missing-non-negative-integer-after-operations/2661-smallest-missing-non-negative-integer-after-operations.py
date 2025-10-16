class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainders = {}
        for num in nums:
            remainder = num%value
            remainders[remainder] = remainders.get(remainder, 0) + 1
        
        for i in range(len(nums) + 1):
            remainder = i%value
            if remainders.get(remainder, 0) == 0:
                return i
            
            remainders[remainder] -= 1
        
        
        