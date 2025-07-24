class Solution:
    def is_valid(self, target, arr, k):
        sumi = 0
        for i in range(len(arr)):
            sumi += arr[i]
            if sumi > target:
                k -= 1
                sumi = arr[i]
        return k > 0

    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        while r > l:
            mid = (l + r) // 2
            if self.is_valid(mid, nums, k):
                r = mid
            else:
                l = mid + 1
        return l