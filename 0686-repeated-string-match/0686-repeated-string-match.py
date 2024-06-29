class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        s = a
        while len(a) <= 20000:
            if b in a:
                return count
            count += 1
            a += s
        return -1