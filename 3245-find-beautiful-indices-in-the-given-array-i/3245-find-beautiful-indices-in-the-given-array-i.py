class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        lps_a = self.returnLPS(a)
        lps_b = self.returnLPS(b)

        index_a = self.matchingIndex(lps_a, s, a)
        index_b = self.matchingIndex(lps_b, s, b)

        i = j = 0
        ans = []
        
        if index_b == []:
            return []
        for i in index_a:
            b1 = bisect.bisect_right(index_b, i + k)
            b2 = bisect.bisect_left(index_b, i - k)
            if(b1!=b2):
                ans.append(i)
        return ans
    
    def returnLPS(self, arr):
        n = len(arr)
        lps = [0 for i in range(n)]
        prevLPS, i = 0, 1
        while i < n:
            if arr[prevLPS] == arr[i]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS:
                prevLPS = lps[prevLPS - 1]
            else:
                i += 1
        return lps
    
    def matchingIndex(self, lps, s, a):
        collection = []
        n, m = len(s), len(a)
        i = j = 0

        while i < n and j < m:
            if s[i] == a[j]:
                i += 1
                j += 1
                if j == m:
                    j = lps[j - 1]
                    collection.append(i - m)
            elif j:
                j = lps[j - 1]
            else:
                i += 1
        return collection
                    

        