class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: if n is 0, return 1
        if n == 0:
            return 1
        
        # If n is negative, use the reciprocal of the result
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x
            # Square x and halve n
            x *= x
            n //= 2
        
        return result