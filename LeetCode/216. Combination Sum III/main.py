from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
    
        def backtrack(start, combination, remaining_sum):
            # Base case: if the combination size equals k and remaining_sum is 0
            if len(combination) == k and remaining_sum == 0:
                result.append(combination[:])  # Add a copy of the combination
                return
            
            # Base case: if the combination size exceeds k or remaining_sum is negative
            if len(combination) > k or remaining_sum < 0:
                return
            
            # Explore all numbers from start to 9
            for i in range(start, 10):
                combination.append(i)  # Include the current number
                backtrack(i + 1, combination, remaining_sum - i)  # Recurse with the next number
                combination.pop()  # Backtrack (remove the current number)
        
        backtrack(1, [], n)  # Start with 1, empty combination, and target sum n
        return result