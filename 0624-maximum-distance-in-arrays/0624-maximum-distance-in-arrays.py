class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini, maxi = inf, -inf
        result = 0
        for i in range(len(arrays)):
            result = max(result, arrays[i][-1] - mini, maxi - arrays[i][0])
            mini = min(mini, arrays[i][0])
            maxi = max(maxi, arrays[i][-1])
        return result
        