from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        
        # Precompute all palindromic substrings using DP
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True  # Single character is always a palindrome
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
        
        def backtrack(start, path):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return result