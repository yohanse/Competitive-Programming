class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def rec(amount, index):
            

            if index == len(coins):
                return 1 if amount == 0 else 0

            result = 0
            for k in range(amount // coins[index] + 1):
                result += rec(amount - k*coins[index], index + 1)
            return result

        return rec(amount, 0)
            
        


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[0 for i in range(n + 1)] for j in range(amount + 1)]
#         dp[0][0] = 1
#         for money in range(1, amount + 1):
#             for coin in range(n):
#                 for k in range(money//coins[coin] + 1):
#                     print(money, k, coins[coin], dp[money - k*coins[coin]][coin])
#                     dp[money][coin + 1] += dp[money - k*coins[coin]][coin]
               
#         print(dp)
#         return dp[-1][-1] 