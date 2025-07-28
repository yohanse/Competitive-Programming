class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @lru_cache
        def min_calc(p1, p2):
            if p1 == n:
                return m - p2
            
            if p2 == m:
                return n - p1
            
            if word1[p1] == word2[p2]:
                return min_calc(p1 + 1, p2 + 1)
            
            return min(min_calc(p1 + 1, p2), min_calc(p1, p2 + 1), min_calc(p1 + 1, p2 + 1)) + 1
        return min_calc(0, 0)
        