class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n > 1:
            n = n / 3
            if n != int(n):
                return False
            n = int(n)
        
        return n == 1
