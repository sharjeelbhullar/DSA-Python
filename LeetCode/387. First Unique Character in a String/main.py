class Solution:
    def firstUniqChar(self, s: str) -> int:
         # Step 1: Count the frequency of each character using a hashmap
        freq_map = {}
        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        
        # Step 2: Find the first unique character by checking frequencies
        for i, char in enumerate(s):
            if freq_map[char] == 1:
                return i  # Return the index of the first unique character
        
        # Step 3: If no unique character exists, return -1
        return -1
            
