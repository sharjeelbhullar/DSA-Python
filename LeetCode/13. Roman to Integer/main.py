class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        ans = 0
        for i in range(len(s) - 1):
            if numerals[s[i]] < numerals[s[i + 1]]:
                ans -= numerals[s[i]]
            else:
                ans += numerals[s[i]]
        ans += numerals[s[-1]]
        return ans
