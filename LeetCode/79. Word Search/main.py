from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            
            # Mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # Explore all four directions
            if (backtrack(i + 1, j, index + 1) or
                backtrack(i - 1, j, index + 1) or
                backtrack(i, j + 1, index + 1) or
                backtrack(i, j - 1, index + 1)):
                return True
            
            # Backtrack
            board[i][j] = temp
            return False
        
        # Iterate through each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

   