class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = {0:1}
        index = nums.index(k)

        count = 0
        for i in range(index - 1, -1, -1):
            count += 1 if nums[i] > k else -1
            left[count] = left.get(count, 0) + 1
        
        count = ans = 0
        for i in range(index + 1, len(nums)):
            count += 1 if nums[i] > k else -1
            ans = ans + left.get(-count, 0) + left.get(1 - count, 0)
        
        return ans + left.get(0, 0) + left.get(1, 0)