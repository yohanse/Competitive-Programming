class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0 for i in range(n + 1)]
        right = [0 for i in range(n + 1)]

        for i in range(n):
            left[i + 1] = left[i]
            if nums[i] == 0:
                left[i + 1] += 1

            right[n - i - 1] = right[n - i]
            if nums[n - i - 1] == 1:
                right[n - i - 1] += 1
        
        for i in range(n + 1):
            left[i] += right[i]
        
        r = max(left)
        ans = []
        for i in range(n + 1):
            if r == left[i]:
                ans.append(i)
        return ans
        