class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0

        for letter in count:
            ans = ans + (count[letter] // 2)*2
        
        if ans != len(s):
            return ans + 1
        return ans