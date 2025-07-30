class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.tic_tac_toe_board = [[-1 for _ in range(n)] for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        self.tic_tac_toe_board[row][col] = player
        if self.do_i_win(row, col, player):
            return player
        return 0
    
    def do_i_win(self, row, col, player):
        for i in range(self.size):
            if self.tic_tac_toe_board[row][i] != player:
                break
        else:
            return True

        for i in range(self.size):
            if self.tic_tac_toe_board[i][col] != player:
                break
        else:
            return True
        
        if row - col == 0:
            for i in range(self.size):
                if self.tic_tac_toe_board[i][i] != player:
                    break
            else:
                return True
            
        if row + col == self.size - 1:
            for i in range(self.size):
                if self.tic_tac_toe_board[-i - 1][i] != player:
                    break
            else:
                return True
        
        return False
        
        
        



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)