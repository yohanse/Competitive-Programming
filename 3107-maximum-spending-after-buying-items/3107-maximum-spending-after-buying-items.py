class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        n, m = len(values), len(values[0])

        heap = []
        for i in range(n):
            heappush(heap, (-values[i][0], 0, i))
        
        ans = 0
        for i in range(n*m, 0, -1):
            value, col, row = heappop(heap)
            ans += (-value*i)
            if col + 1 != m:
                heappush(heap, (-values[row][col + 1], col + 1, row))
            
        return ans
        