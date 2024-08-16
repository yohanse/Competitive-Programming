class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(number):
            return int(number**0.5)**2 == number

        n = len(nums)
        final = 2**n - 1
        @cache
        def rec(bit, prev):
            if bit == final:
                return 1

            ans = 0
            used = set()
            for i in range(n):
                current = 1 << i
                if current & bit == 0 and is_square(prev + nums[i]) and nums[i] not in used:
                    ans += rec(bit | current, nums[i])
                    used.add(nums[i])
            return ans

        res = 0
        used = set()
        for i in range(n):
            if nums[i] not in used:
                res += rec(1 << i, nums[i])
                used.add(nums[i])
        return res

        