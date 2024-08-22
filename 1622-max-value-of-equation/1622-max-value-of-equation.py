class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        ans = -inf
        for i in range(len(points)):
            while heap and points[i][0] - heap[0][1] > k:
                heappop(heap)
            
            if heap:
                ans = max(ans, sum(points[i]) - heap[0][0])
            heappush(heap, [points[i][0] - points[i][1], points[i][0]])
        return ans