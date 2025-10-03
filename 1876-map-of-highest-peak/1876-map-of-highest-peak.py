class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        from collections import deque
        rows, cols = len(isWater), len(isWater[0])
        heights = [[0 for _ in range(cols)] for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    isWater[r][c] = "#"
        
        while queue:
            r, c = queue.popleft()

            for dx, dy in directions:
                x, y = r + dx, c + dy

                if -1 < x < rows and -1 < y < cols and isWater[x][y] != "#":
                    isWater[x][y] = "#"
                    queue.append((x, y))
                    heights[x][y] = 1 + heights[r][c]
        
        return heights
