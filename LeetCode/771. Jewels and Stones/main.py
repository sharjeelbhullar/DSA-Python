from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count = Counter(stones)  
        return sum(stone_count[j] for j in jewels if j in stone_count)  
