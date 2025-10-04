class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        # nums[p] * nums[r] == nums[q] * nums[s]
        # nums[p] / nums[q] = nums[s] / nums[r]
        # nums[p] / nums[q] = res
        valid_indices = {}

        count = 0
        for r in range(4, len(nums)):
            for p in range(r - 3):
                res = nums[p] / nums[r - 2]
                valid_indices[res] = valid_indices.get(res, 0) + 1
            
            for s in range(r + 2, len(nums)):
                res = nums[s] / nums[r]
                count += valid_indices.get(res, 0)
            
            
        return count
            



