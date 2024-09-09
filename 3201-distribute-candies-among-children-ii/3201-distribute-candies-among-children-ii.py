class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        combination = 0
        for i in range(min(limit, n) + 1):
            if n - i <= 2*limit:
                l, r = max(n - i- limit, 0), min(limit, n - i)
                combination += r - l + 1
        return combination