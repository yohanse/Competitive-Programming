class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        heap = [(0, 0, 0)]
        time = [[float("inf") for _ in range(m)] for _ in range(n)]
        time[0][0] = 0
        
        while heap:
            curr_time, r, c = heapq.heappop(heap)
            if r == n - 1 and c == m - 1:
                return curr_time
            
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if -1 < x < n and -1 < y < m and time[x][y] > max(curr_time + 1, grid[x][y] + (grid[x][y] - curr_time - 1)%2):
                    time[x][y] = max(curr_time + 1, grid[x][y] + (grid[x][y] - curr_time - 1)%2)
                    heapq.heappush(heap, (time[x][y], x, y))
        
        
