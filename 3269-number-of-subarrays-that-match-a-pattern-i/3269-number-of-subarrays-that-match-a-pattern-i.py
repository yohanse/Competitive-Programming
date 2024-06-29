class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        lps = [0 for i in range(m)]

        prevLPS, i = 0, 1
        while i < m:
            if pattern[i] == pattern[prevLPS]:
                lps[i] = prevLPS + 1
                i += 1
                prevLPS += 1
            elif prevLPS == 0:
                    i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        array = [0 for i in range(n - 1)]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                array[i - 1] = 1
            
            if nums[i] < nums[i - 1]:
                array[i - 1] = -1

        i = j = count = 0
        while i < n - 1 and j < m:
            if array[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    j = lps[j - 1]
                    count += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]
        
        return count
