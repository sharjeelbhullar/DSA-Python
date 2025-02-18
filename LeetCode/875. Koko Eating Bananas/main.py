from math import ceil
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        def hours_needed(speed):
            return sum(ceil(pile / speed) for pile in piles)
        
        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid 
            else:
                left = mid + 1

        return left 
