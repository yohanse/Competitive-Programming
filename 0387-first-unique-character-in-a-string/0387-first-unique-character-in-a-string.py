class Solution:
    def find_ord_value(self, letter):
        return ord(letter) - ord('a')
    def firstUniqChar(self, s: str) -> int:
        freq = [0 for _ in range(26)]
        for letter in s:
            freq[self.find_ord_value(letter)] += 1
        
        for i in range(len(s)):
            if freq[self.find_ord_value(s[i])] == 1:
                return i
        return -1
        