class Solution:
    def minOperations(self, k: int) -> int:
        ans = inf
        for x in range(1, k + 1):
            ans = min(ans, x + (ceil(k / x)) - 2)
        return ans
        