class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        lps_group = []
        for array in groups:
            lps_group.append(self.returnLPS(array))
        
        rows, n = len(groups), len(nums)
        r = c = i = 0
        while r < rows and i < n:
            if groups[r][c] == nums[i]:
                c += 1
                i += 1
                if c == len(groups[r]):
                    c = 0
                    r += 1
            elif c == 0:
                i += 1
            else:
                c = lps_group[r][c - 1]
        return rows == r

        
    
    def returnLPS(self, array):
        prevLPS, i, n = 0, 1, len(array)
        lps = [0 for i in range(n)]

        while i < n:
            if array[i] == array[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        return lps