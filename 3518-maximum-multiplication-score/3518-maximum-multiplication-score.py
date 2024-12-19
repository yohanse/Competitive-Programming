class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        maxi = [-inf, -inf, -inf, -inf]
        for i in range(len(b)):
            if i > 2:
                maxi[3] = max(maxi[3], maxi[2] + a[3]*b[i])

            if i > 1:
                maxi[2] = max(maxi[2], maxi[1] + a[2]*b[i])
            
            if i:
                maxi[1] = max(maxi[1], maxi[0] + a[1]*b[i])
            maxi[0] = max(maxi[0], a[0]*b[i])
        return maxi[-1]