class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        sumi = 2 ** (len(nums)) - 1
        memo = {}
        modulo = 10**9 + 7
        def rec(perm, last):
            if perm == sumi:
                return 1
            
            if (perm, last) in memo:
                return memo[(perm, last)]

            memo[(perm, last)] = 0
            for i in range(len(nums)):
                if (perm & 1 << i) == 0 and (last % nums[i] == 0 or nums[i] % last == 0):
                    memo[(perm, last)] += rec(perm | 1 << i, nums[i])
            
            return memo[(perm, last)]
        return rec(0, 0) % modulo
        