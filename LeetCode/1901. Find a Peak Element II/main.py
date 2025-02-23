from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1

        while left <= right:
            mid_col = (left + right) // 2

            max_row = max(range(m), key=lambda r: mat[r][mid_col])

            left_neighbor = mat[max_row][mid_col - 1] if mid_col > 0 else -1
            right_neighbor = mat[max_row][mid_col + 1] if mid_col < n - 1 else -1

            if mat[max_row][mid_col] > left_neighbor and mat[max_row][mid_col] > right_neighbor:
                return [max_row, mid_col]
            
            if left_neighbor > mat[max_row][mid_col]:
                right = mid_col - 1
            else:
                left = mid_col + 1

        return [-1, -1]  
