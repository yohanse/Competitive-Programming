class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mandatory_step = abs(endPos - startPos)
        MODULO = 10**9 + 7

        if k >= mandatory_step and (k - mandatory_step) % 2 == 0:
            return comb(k, mandatory_step + (k - mandatory_step) // 2) % MODULO
        return 0
        