class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = 1
        ngFlag = 0
        if n < 0:
            ngFlag = 1
            n = n * -1
        while n != 0:
            if n & 1:
                result *= x
            x = x * x
            
            n = n // 2
            
        if ngFlag:
            result = 1 / result
        
        return result