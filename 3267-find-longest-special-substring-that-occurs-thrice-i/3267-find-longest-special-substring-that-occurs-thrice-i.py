class Solution:
    def maximumLength(self, s: str) -> int:
        if max(Counter(s).values()) < 3:
            return -1

        def good_function(mid):
            letter = [0 for i in range(26)]
            count = 1
            for i in range(1, len(s)):
                if s[i] != s[i - 1]:
                    letter[ord(s[i - 1]) - ord('a')] += max(0, count - mid + 1)
                    count = 0
                count += 1
            letter[ord(s[-1]) - ord('a')] += max(0, count - mid + 1)
            return max(letter) > 2

        l, r = 1, len(s)
        while l < r:
            mid = (l + r + 1) // 2
            if good_function(mid):
                l = mid
            else:
                r = mid - 1
        return l


        