class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        def backtrack(index, subset):
            if n == index:
                subsets.append(subset.copy())
                return
            
            backtrack(index + 1, subset)
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
        
        backtrack(0, [])
        return subsets
        
        