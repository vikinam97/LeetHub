class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Solution - using divide power /2
        # Time -> O(log(n))
        # Space -> O(1)
        
        result = 1
        ngFlag = 0
        # to handle neg power
        if n < 0:
            ngFlag = 1
            n = n * -1
            
        while n != 0:
            if n & 1:
                result *= x
            x = x * x
            n = n // 2
        
        # neg power = 1 / positive power
        if ngFlag:
            result = 1 / result
        
        return result