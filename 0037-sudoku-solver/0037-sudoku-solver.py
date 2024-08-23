class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def empty_space(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        return i,j
            return False
        
        def can_not(board,i,j):
            num=[0,0,0,0,0,0,0,0,0]
            for x in range(9):
                key=board[i][x]
                if key!='.' and num[int(key)-1]==0:
                    num[int(key)-1]=1
            for x in range(9):
                key=board[x][j]
                if key!='.' and num[int(key)-1]==0:
                    num[int(key)-1]=1
            i=(i//3)*3
            j=(j//3)*3
            for x in range(i,i+3):
                for y in range(j,j+3):
                    key=board[x][y]
                    if key!='.' and num[int(key)-1]==0:
                        num[int(key)-1]=1
            return num
        
        def solution(board):
            if empty_space(board)==False:
                return board
            i,j=empty_space(board)
            num=can_not(board,i,j)
            for k in "123456789":
                if num[int(k)-1]!=1:
                    board[i][j]=k
                    if solution(board):
                        return solution(board)
                    else:
                        board[i][j]='.'
        return solution(board)