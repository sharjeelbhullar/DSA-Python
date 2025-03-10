from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates
        result = []
        
        def backtrack(index, path):
            result.append(path)  # Add the current subset to the result
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue  # Skip duplicates
                backtrack(i + 1, path + [nums[i]])  # Recurse with the next index
        
        backtrack(0, [])
        return result