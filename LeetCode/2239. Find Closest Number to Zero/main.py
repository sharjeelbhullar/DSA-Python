from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')  # Initialize with a large value (infinity)

        for num in nums:
            # Check if the current number is closer to zero
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        
        return closest