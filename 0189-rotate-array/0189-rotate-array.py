class Solution:
    def reverse(self, l, r):
        while l < r:
            self.nums[l], self.nums[r] = self.nums[r], self.nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        
        n = len(nums)
        k %= n

        if k != 0:
            self.reverse(0, n - 1)
            self.reverse(0, k - 1)
            self.reverse(k, n - 1)