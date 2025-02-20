class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def predict(l, r):
            if l >= r:
                return 0

            ans = inf
            for i in range(l, r + 1):
                ans = min(ans, max(predict(l, i - 1), predict(i + 1, r)) + i)
            return ans

        return predict(1, n)
        