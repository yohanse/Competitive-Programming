class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j, target, count):

            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == -1:
                return 0

            
            if grid[i][j] == 2:
                if target == count:
                    return 1
                return 0

            grid[i][j] = -1

            num = ( dfs(i + 1, j, target, count + 1) +
                    dfs(i - 1, j, target, count + 1) + 
                    dfs(i, j + 1, target, count + 1) + 
                    dfs(i, j - 1, target, count + 1))
            
            grid[i][j] = 0
            return num

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_row, start_col = r, c
                if grid[r][c] == 0:
                    count += 1
        return dfs(start_row, start_col, count + 1, 0)

        

        

        