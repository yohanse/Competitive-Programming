class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        keys = set(["a", "b", "c", "d", "e", "f"])
        locks = set(["A", "B", "C", "D", "E", "F"])
        count_key = 0      
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "@":
                    queue.append((r, c, "", 0))
                    visited.add((r, c, ""))

                if grid[r][c] in keys:
                    count_key += 1

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c, key, moves = queue.popleft()
            if len(key) == count_key:
                return moves
            print(r, c, key)
            for dx, dy in direction:
                x = r + dx
                y = c + dy
                if -1 < x < n and -1 < y < m and grid[x][y] != "#" and (x, y, key) not in visited:
                    if grid[x][y] == "." or grid[x][y] == "@":
                        queue.append((x, y, key, moves + 1))
                        visited.add((x, y, key))
                    
                    if grid[x][y] in keys:
                        if  grid[x][y] not in key:
                            keycopy = key + grid[x][y]
                            keycopy = list(keycopy)
                            keycopy.sort()
                            keycopy = "".join(keycopy)
                            queue.append((x, y, keycopy, moves + 1))
                            visited.add((x, y, keycopy))
                        else:
                            queue.append((x, y, key, moves + 1))
                            visited.add((x, y, key))
                    
                    
                    
                    
                    if grid[x][y] in locks and grid[x][y].lower() in key:
                        queue.append((x, y, key, moves + 1))
                        visited.add((x, y, key))


        return -1