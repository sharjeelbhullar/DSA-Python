from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check the column for any other queen
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True

        def backtrack(row):
            if row == n:
                # All queens are placed successfully
                solutions.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(board, row, col):
                    # Place the queen
                    board[row][col] = 'Q'
                    # Move to the next row
                    backtrack(row + 1)
                    # Backtrack (remove the queen)
                    board[row][col] = '.'
        
        # Initialize the chessboard
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        backtrack(0)
        return solutions