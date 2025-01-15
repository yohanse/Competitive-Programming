class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = {}
        def IsMatch(i, j):
            if i == n and j == m:
                return True
            
            if j == m:
                return False
            
            if i == n:
                for k in range(j, m):
                    if p[k] != "*":
                        return False
                return True
            
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = False
            if s[i] == p[j] or p[j] == "?":
                dp[(i, j)] = IsMatch(i + 1, j + 1)
            
            if p[j] == "*":
                dp[(i, j)] = IsMatch(i, j + 1) or  IsMatch(i + 1, j + 1) or IsMatch(i + 1, j)
            return dp[(i, j)]

        return IsMatch(0, 0)
        