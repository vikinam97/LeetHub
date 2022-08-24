class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        log = math.log10(n) / math.log10(3)
        return log == int(log)

class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n > 1:
            n = n / 3
            if n != int(n):
                return False
            n = int(n)
        
        return n == 1
