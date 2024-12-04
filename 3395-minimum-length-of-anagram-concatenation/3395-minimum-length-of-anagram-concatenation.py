class Solution:
    def minAnagramLength(self, s: str) -> int:
        factors = []
        num = ans = len(s)
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
       
        for factor in factors:
            
            flag = True
            for i in range(factor, len(s), factor):
                initial = [0 for i in range(26)]
                for j in range(factor):
                    initial[ord(s[j]) - ord("a")] += 1

                for j in range(i, i + factor):
                    initial[ord(s[j]) - ord("a")] -= 1
                    if initial[ord(s[j]) - ord("a")] < 0:
                        flag = False
                        break
            if flag:
                ans = min(ans, factor)
        return ans
        