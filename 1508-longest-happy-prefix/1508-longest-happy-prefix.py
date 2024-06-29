class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0 for i in range(n)]

        slow, fast = 0, 1
        while fast < n:
            if s[fast] == s[slow]:
                lps[fast] = slow + 1
                slow += 1
                fast += 1
            elif slow == 0:
                fast += 1
            else:
                slow = lps[slow - 1]
        return s[:lps[-1]]