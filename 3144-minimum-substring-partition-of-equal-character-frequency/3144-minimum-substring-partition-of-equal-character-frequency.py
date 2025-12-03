class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [inf for _ in range(n + 1)]
        dp[0] = 0
        for i in range(n):
            letters = [0 for _ in range(26)]
            unique_char = max_freq = max_count = 0
            for j in range(i, n):
                char_index = ord(s[j]) - ord("a")
                letters[char_index] += 1

                if letters[char_index] == 1:
                    unique_char += 1
                
                if letters[char_index] == max_freq:
                    max_count += 1
                
                if letters[char_index] > max_freq:
                    max_freq = letters[char_index]
                    max_count = 1

                if unique_char == max_count:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)
       
        return dp[-1]