class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        leng_word = len(word)

        directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]

        def dfs(r, c, index):
            if index == leng_word:
                return True
            
            if r < 0 or r == rows or c < 0 or c == cols:
                return False
            
            
            temp = board[r][c]
            board[r][c] = "#"
            for dx, dy in directions:
                x = r + dx
                y = c + dy

                if x < 0 or x == rows or y < 0 or y == cols or board[x][y] == "#":
                    continue

                if board[x][y] == word[index] and dfs(x, y, index + 1):
                    board[r][c] = temp
                    return True
            board[r][c] = temp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True
        return False
        