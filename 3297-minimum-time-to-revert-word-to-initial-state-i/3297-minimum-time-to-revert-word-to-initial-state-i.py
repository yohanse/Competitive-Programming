class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        time = 1
        n = len(word)
        for i in range(k, n, k):
            for j in range(i, n):
                if word[j] != word[j - i]:
                    break
            else:
                return time
            time += 1
        return time