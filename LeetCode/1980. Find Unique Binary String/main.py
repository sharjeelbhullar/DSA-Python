from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        unique_binary = []

        for i in range(n):
            flipped_bit = '1' if nums[i][i] == '0' else '0'
            unique_binary.append(flipped_bit)

        return ''.join(unique_binary)
