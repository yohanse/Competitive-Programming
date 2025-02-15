class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        def rec(l, r, i):
            if l >= r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            memo[(l, r)] = 0
            if nums[l] + nums[l + 1] == i:
                memo[(l, r)] = max(memo[(l, r)], 1 + rec(l + 2, r, i))
            if nums[r] + nums[r - 1] == i:
                memo[(l, r)] = max(memo[(l, r)], 1 + rec(l, r - 2, i))
            if nums[r] + nums[l] == i:
                memo[(l, r)] = max(memo[(l, r)], 1 + rec(l + 1, r - 1, i))
            return memo[(l, r)]

        max_op = 0

        memo = {}
        max_op = max(max_op, rec(0, n - 1, nums[0] + nums[1]))
        memo = {}
        max_op = max(max_op, rec(0, n - 1, nums[0] + nums[-1]))
        memo = {}
        max_op = max(max_op, rec(0, n - 1, nums[-1] + nums[-2]))
        return max_op