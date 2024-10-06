class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i, N = 0, len(words)
        ans = []
        while i < N:
            current, count = maxWidth, 0
            ans.append([])
            while i < N and current - len(words[i]) - count > -1:
                ans[-1].append(words[i])
                current -= len(words[i])
                count += 1
                i += 1
            ans[-1].append([count - 1, current])

        result = []
        for i in range(len(ans) - 1):
            result.append("")
            numWord, freeSpace = ans[i][-1]
            if numWord == 0:
                space = " " * freeSpace
                result[-1] = ans[i][-2] + space
            else:
                even, odd = freeSpace // numWord, freeSpace % numWord
                space = " " * even

                for j in range(len(ans[i]) - 2):
                    word = ans[i][j] + space
                    if odd > 0:
                        word += " "
                        odd -= 1
                    result[i] += word
                result[i] += ans[i][-2]
        result.append("")
        for i in range(len(ans[-1]) - 1):
            result[-1] += ans[-1][i] + " "
        
        numWord, freeSpace = ans[-1][-1]
        freeSpace -= numWord
        space = " " * freeSpace
        result[-1] = result[-1][:-1] + space

        return result