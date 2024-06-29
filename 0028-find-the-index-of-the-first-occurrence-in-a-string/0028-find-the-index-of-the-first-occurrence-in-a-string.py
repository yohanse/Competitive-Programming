class Solution:
    def strStr(self, a: str, b: str) -> int:
        alpha = 26
        hashBase = currHash = 0
        lengthA, lengthB = len(a), len(b)

        def hashAlpha(char):
            return ord(char) - ord("a") + 1

        def addLast(hashValue, char):
            return hashValue * alpha + hashAlpha(char)

        def pollLast(hashValue, char, k):
            return hashValue - hashAlpha(char) * alpha ** k

        for i in b:
            hashBase = addLast(hashBase, i)

        for i in range(lengthA):
            currHash = addLast(currHash, a[i])

            if currHash == hashBase:
                return i - lengthB + 1

            if i >= len(b) - 1:
                currHash = pollLast(currHash, a[i - lengthB + 1], lengthB - 1)
                
        return -1             