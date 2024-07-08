class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        alphabet = [0 for i in range(26)]
        for char in s:
            count = alphabet[ord(char) - ord("a")]
            for i in range(26):
                if abs(ord(char) - ord("a") - i) <= k:
                    count = max(count, alphabet[i] + 1)
            alphabet[ord(char) - ord("a")] = count
        return max(alphabet)