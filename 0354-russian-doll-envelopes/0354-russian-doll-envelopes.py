class Solution:
    def binary_search(self, weights, weight):
        l, r = 0, len(weights) - 1
        while l < r:
            mid = (l + r) // 2
            if weights[mid] >= weight:
                r = mid
            else:
                l = mid + 1
        return l

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        weights = []
        for i in range(len(envelopes)):
            weights.append(envelopes[i][1])
        
        print(envelopes)
        print(weights)

        dp = [weights[0]]
        for weight in weights[1:]:
            if weight > dp[-1]:
                dp.append(weight)
            else:
                index = self.binary_search(dp, weight)
                dp[index] = weight

        return len(dp)