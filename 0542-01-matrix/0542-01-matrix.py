class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    mat[r][c] = -1
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dx, dy in directions:
                x = r + dx
                y = c + dy

                if -1 < x < rows and -1 < y < cols and mat[x][y] > 0:
                    mat[x][y] = mat[r][c] - 1
                    queue.append((x, y))
        
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = -mat[r][c] - 1
        
        return mat