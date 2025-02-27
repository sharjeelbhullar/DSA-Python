class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total_beauty = 0
        
        for i in range(n):
            freq = [0] * 26  # Frequency map for characters a-z
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1  # Update frequency
                max_freq = max(freq)
                min_freq = min(f for f in freq if f > 0)  # Ignore zero frequencies
                total_beauty += max_freq - min_freq
        
        return total_beauty