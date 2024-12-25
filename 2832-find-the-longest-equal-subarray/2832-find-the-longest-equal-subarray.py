class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        reverse_freq = {0:1}
        map_freq = {}
        l = ans = max_freq = 0
        for r in range(n):
            map_freq[nums[r]] = map_freq.get(nums[r], 0) + 1
            reverse_freq[map_freq[nums[r]]] = reverse_freq.get(map_freq[nums[r]], 0) + 1
            max_freq = max(max_freq, map_freq[nums[r]])
            while reverse_freq.get(max(0, r - l + 1 - k), 0) == 0:
                map_freq[nums[l]] -= 1
                reverse_freq[map_freq[nums[l]] + 1] -= 1
                if reverse_freq[map_freq[nums[l]] + 1] == 0:
                    max_freq -= 1
                l += 1
            
            ans = max(ans, max_freq)
        return ans