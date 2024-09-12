class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        for i in range(1, 11):
            if str(num)[-1] == str(k*i)[-1] and num >= k*i:
                return i
        return -1
        