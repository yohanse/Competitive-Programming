class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = [0] * 26
        for i in letters:
            count[ord(i) - ord("a")] += 1

        res, N = [0], len(words)

        def back(index, count, ans):
            if index == N:
                res[0] = max(res[0], ans)
                return 

            temp = count.copy()
            temp_ans = 0
            for letter in words[index]:
                i = ord(letter) - ord("a")
                count[i] -= 1
                if count[i] == -1:
                    break
                temp_ans += score[i]
            else:
                back(index + 1, count, ans + temp_ans)
            count = temp

            back(index + 1, count, ans)

        back(0, count, 0)
        return res[0]
