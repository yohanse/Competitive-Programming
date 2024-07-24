class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        set_col = set()
        set_dig = set()
        set_ant = set()

        def canPut(r, c):
            return not (c in set_col or (r + c) in set_dig or ((r - c) in set_ant))

        board = [["." for i in range(n)] for j in range(n)]
        result = []
        def bactracking(row):
            if row == n:
                boardCopy = []
                for i in range(n):
                    string = "".join(board[i])
                    boardCopy.append(string)
                result.append(boardCopy)
                return 
            
            for col in range(n):
                if canPut(row, col):
                    set_col.add(col)
                    set_dig.add(row + col)
                    set_ant.add(row - col)
                    board[row][col] = "Q"
                    bactracking(row + 1)
                    set_col.remove(col)
                    set_dig.remove(row + col)
                    set_ant.remove(row - col)
                    board[row][col] = "."
        
        bactracking(0)
        return result







        