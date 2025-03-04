class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones)
        dp = {}
        def rec(index, k):
            if index == N - 1:
                return True
            if (index, k) in dp:
                return dp[(index, k)]
            
            for i in range(index + 1, N):
                if (index == 0 and stones[i] - stones[index] == 1 and rec(i, stones[i] - stones[index])) or (index != 0 and abs(k - (stones[i] - stones[index])) < 2 and rec(i, stones[i] - stones[index])):
                    dp[(index, k)] = True
                    return True

            dp[(index, k)] = False
            return False


        return rec(0, 1)
