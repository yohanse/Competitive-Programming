class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        min_operation = n
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if int(num[j] + num[i]) % 25 == 0:
                    min_operation = min(min_operation, n - j - 2)
                    
        if min_operation == n and "0" in num:
            return n - 1
        return min_operation