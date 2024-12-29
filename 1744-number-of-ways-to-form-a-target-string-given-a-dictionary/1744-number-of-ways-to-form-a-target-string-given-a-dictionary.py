class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        modulo = 10**9 + 7
        word_leng = len(words[0])
        occurence = [[0 for _ in range(26)] for _ in range(word_leng)]

        for i in range(len(words)):
            for j in range(word_leng):
               occurence[j][ord(words[i][j]) - ord("a")] += 1

        def rec(index, index_occurence):
            if index == len(target):
                return 1
            
            if index_occurence == word_leng:
                return 0
            
            return occurence[index_occurence][ord(target[index]) - ord("a")]*rec(index + 1, index_occurence + 1) + rec(index, index_occurence + 1)
        
        dp = [[0 for i in range(word_leng + 1)] for j in range(len(target) + 1)]
        dp[-1] = [1 for i in range(word_leng + 1)]

        for index in range(len(target) - 1, -1, -1):
            for index_occurence in range(word_leng - 1, -1, -1):
                dp[index][index_occurence] = occurence[index_occurence][ord(target[index]) - ord("a")]*dp[index + 1][index_occurence + 1] + dp[index][index_occurence + 1]
        return dp[0][0] % modulo
        