from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums 
    
        for i in range(1, len(nums)):  # Start from index 1
            nums[i] = nums[i] + nums[i - 1]  # Add the previous sum
        return nums