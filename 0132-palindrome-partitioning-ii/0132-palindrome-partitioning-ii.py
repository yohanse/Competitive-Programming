class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        dp = {}
        isPalindrome = [[False for i in range(N)] for j in range(N)]
        def check(l, r):
            print(l, r)
            return True

        for i in range(N):
            l = r = i 
            print(i)
            while check(l, r) and l > -1 and r < N and s[r] == s[l]:
                isPalindrome[l][r] = True
                l, r = l - 1, r + 1
        
        for i in range(1, N):
            l, r = i - 1, i 
            while l > -1 and r < N and s[r] == s[l]:
                isPalindrome[l][r] = True
                l, r = l - 1, r + 1

        def rec(index):
            if index == N:
                return 0

            if index in dp:
                return dp[(index)]

            dp[(index)] = inf
            for i in range(index, N):
                if isPalindrome[index][i]:
                    dp[(index)] = min(dp[(index)], 1 + rec(i + 1))
            return dp[(index)]
        return rec(0) - 1
