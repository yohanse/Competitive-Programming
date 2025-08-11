class Solution:
    def nextGreaterElement(self, n: int) -> int:
        max_number = 2**31 - 1

        digits = list(str(n))

        for i in range(len(digits) - 2, -1, -1):
            if int(digits[i]) < int(digits[i + 1]):
                for j in range(len(digits) - 1, i, -1):
                    if int(digits[j]) > int(digits[i]):
                        digits[i], digits[j] = digits[j], digits[i]
                        break
                
                l, r = i + 1, len(digits) - 1
                while l < r:
                    digits[r], digits[l] = digits[l], digits[r]
                    l += 1
                    r -= 1
                
                num = int("".join(digits))
                if num > max_number:
                    return -1
                return num
        return -1

        