from typing import List
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        # Create an empty 3x3 board
        board = [['' for _ in range(3)] for _ in range(3)]
        
        # Fill the board with moves
        for i, move in enumerate(moves):
            row, col = move
            board[row][col] = 'A' if i % 2 == 0 else 'B'
        
        # Check rows and columns for a winner
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
                return board[0][i]
        
        # Check diagonals for a winner
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            return board[0][2]
        
        # If there are any empty cells, the game is still ongoing
        if len(moves) < 9:
            return "Pending"
        
        # If no winner and the board is full, it's a draw
        return "Draw"
