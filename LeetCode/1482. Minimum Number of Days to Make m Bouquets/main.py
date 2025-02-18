from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1  

        left, right = min(bloomDay), max(bloomDay)
        
        def canMakeBouquets(days):
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0  
                else:
                    flowers = 0  
                
                if bouquets >= m:
                    return True
            
            return False

        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid  
            else:
                left = mid + 1 

        return left
