class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        dup = x
        if x < 0: return False
        else:
            while(x > 0):
                lastDigit = x % 10
                reverse = reverse * 10 + lastDigit
                x //= 10
            if reverse == dup:
                return True
            else:
                return False
