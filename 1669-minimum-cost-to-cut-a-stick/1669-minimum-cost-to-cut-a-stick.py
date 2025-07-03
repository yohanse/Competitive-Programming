class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        dp = {}
        def rec(left, right, left1, right1):
            if left == right:
                return right1 - left1
            
            if right < left:
                return 0

            if (left, right, left1, right1) in dp:
                return dp[(left, right, left1, right1)]
                
            ans = inf
            for i in range(left, right + 1):
                ans = min(ans, rec(left, i - 1, left1, cuts[i]) + rec(i + 1, right, cuts[i], right1) + right1 - left1)
            dp[(left, right, left1, right1)] = ans
            return ans
        
        return rec(0, len(cuts) - 1, 0, n)
