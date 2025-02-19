from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            total = 0  
            required_days = 1  
            for weight in weights:
                if total + weight > capacity:
                    required_days += 1
                    total = 0
                total += weight
            return required_days <= days

        low, high = max(weights), sum(weights)
        
        while low < high:
            mid = (low + high) // 2
            if canShip(mid):
                high = mid  
            else:
                low = mid + 1  
        
        return low
