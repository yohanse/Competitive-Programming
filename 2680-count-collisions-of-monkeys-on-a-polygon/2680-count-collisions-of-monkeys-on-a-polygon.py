class Solution:
    def monkeyMove(self, n: int) -> int:
        MODULO = 10**9 + 7
        return (pow(2, n, MODULO) - 2) % MODULO