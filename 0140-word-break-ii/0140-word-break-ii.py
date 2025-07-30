class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        s_leng = len(s)
        dp = [[] for _ in range(s_leng + 1)]
        dp[0] = [""]

        for i in range(s_leng):
            for word in wordDict:
                begining = i - len(word) + 1
                if len(word) <= i + 1 and dp[begining]:
                    for k in range(begining, i + 1):
                        if s[k] != word[k - begining]:
                            break
                    else:
                        for valid_string in dp[begining]:
                            if begining == 0:
                                dp[i + 1].append(word)
                            else:
                                dp[i + 1].append(f"{valid_string} {word}")
        return dp[-1]
                    


        