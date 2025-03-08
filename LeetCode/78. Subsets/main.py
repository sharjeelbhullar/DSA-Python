from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])
            
            # Explore all possible subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                path.append(nums[i])
                # Move to the next element
                backtrack(i + 1, path)
                # Exclude nums[i] (backtrack)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
