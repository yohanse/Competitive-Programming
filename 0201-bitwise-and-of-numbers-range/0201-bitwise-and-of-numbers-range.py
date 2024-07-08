class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(32):
            value = 1 << i
            if (left & value) and (right & value) and right - left < value:
                ans += value
        return ans
        