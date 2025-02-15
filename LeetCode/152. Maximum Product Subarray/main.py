from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_so_far = min_so_far = result = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            max_so_far = max(nums[i], max_so_far * nums[i])
            min_so_far = min(nums[i], min_so_far * nums[i])
            
            result = max(result, max_so_far)
        
        return result
