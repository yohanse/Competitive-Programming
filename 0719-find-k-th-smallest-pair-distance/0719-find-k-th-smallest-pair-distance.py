class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def good_function(number, k):
            l = 0
            count = 0
            for r in range(n):
                while nums[r] - nums[l] > number:
                    l += 1
                    count += (r - l)
            leng = n - l
            arch = leng*(leng - 1) // 2
            return count + arch >= k

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if good_function(mid, k):
                r = mid
            else:
                l = mid + 1
        return l
