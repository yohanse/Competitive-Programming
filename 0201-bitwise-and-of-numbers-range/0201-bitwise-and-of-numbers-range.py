class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(32):
            if (left & 2**i) and (right & 2**i) and right - left < 2**i:
                ans += 2**i
        return ans
        