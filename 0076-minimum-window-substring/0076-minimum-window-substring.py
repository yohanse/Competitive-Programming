class Solution:
    def is_valid(self, dict_a, dict_b):
        for i in dict_a:
            if dict_a[i] > dict_b.get(i, 0):
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        for letter in t:
            dict_t[letter] = dict_t.get(letter, 0) + 1

        dict_window = {}
        l = 0
        result = [-inf, inf]
        for r in range(len(s)):
            dict_window[s[r]] = dict_window.get(s[r], 0) + 1
            valid = False
            while self.is_valid(dict_t, dict_window):
                dict_window[s[l]] -= 1
                valid = True
                l += 1
            
            if valid and result[1] - result[0] + 1 > r - l + 2:
                result = [l - 1, r]
        if result == [-inf, inf]:
            return ""
        
        return s[result[0]:result[1] + 1]
                