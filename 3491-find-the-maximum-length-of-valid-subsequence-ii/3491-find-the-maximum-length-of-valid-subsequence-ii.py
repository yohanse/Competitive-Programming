class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        modulo_nums = [num%k for num in nums]
       
        ans = 0
        for reminder in range(k):
            pre_modulo = {}
            for r in range(len(nums)):
                previous = reminder - modulo_nums[r]
                if previous < 0:
                    previous += k
                
                pre_modulo[modulo_nums[r]] = max(pre_modulo.get(modulo_nums[r], 0), pre_modulo.get(previous, 0) + 1)
                ans = max(ans, pre_modulo[modulo_nums[r]])
        return ans
        