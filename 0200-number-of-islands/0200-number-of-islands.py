class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()
        num_island = 0

        def bfs(x, y):
            stack = [(x, y)]
            visited.add((x, y))
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    r = x + dx
                    c = y + dy

                    if r == -1 or r == rows or c == -1 or c == cols:
                        continue

                    if (r, c) not in visited and grid[r][c] == "1":
                        stack.append((r, c))
                        visited.add((r, c))  
            return 1 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_island += bfs(r, c)


           
        return num_island   