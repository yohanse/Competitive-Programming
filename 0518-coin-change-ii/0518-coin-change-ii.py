class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def rec(amount, index):
            if amount == 0:
                return 1

            if index == len(coins):
                return 0

            result = 0
            for k in range(amount // coins[index] + 1):
                result += rec(amount - k*coins[index], index + 1)
            return result

        return rec(amount, 0)
            
        