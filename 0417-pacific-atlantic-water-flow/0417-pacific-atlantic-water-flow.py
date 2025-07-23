class Solution:
    def bfs(self, queue, choice, heights, is_connected, n, m):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set(queue)
        while queue:
            r, c = queue.pop()
            is_connected[r][c][choice] = True
            for dx, dy in directions:
                x = r + dx
                y = c + dy

                if -1 < x < n and -1 < y < m and heights[x][y] >= heights[r][c] and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))

        return is_connected

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        is_connected = [[[False, False] for _ in range(m)] for _ in range(n)]

        # Atlantic
        queue = []
        for i in range(n):
            queue.append((i, m - 1))
        for i in range(m):
            queue.append((n - 1, i))
        
        is_connected = self.bfs(queue, 0, heights, is_connected, n, m)
        

        queue = []
        for i in range(n):
            queue.append((i, 0))
        for i in range(m):
            queue.append((0, i))
        
        is_connected = self.bfs(queue, 1, heights, is_connected, n, m)
        
        result = []
        for r in range(n):
            for c in range(m):
                if is_connected[r][c] == [True, True]:
                    result.append((r,c))
        return result
        