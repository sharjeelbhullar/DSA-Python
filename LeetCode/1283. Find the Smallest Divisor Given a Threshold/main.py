from typing import List
from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        def sum_of_divisions(d):
            return sum(ceil(num / d) for num in nums)
        
        while left < right:
            mid = (left + right) // 2
            if sum_of_divisions(mid) <= threshold:
                right = mid  
            else:
                left = mid + 1  
        
        return left
