class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        while n >= 4:
            n = n / 4
            if n != int(n): return False
            n = int(n)
            
        return n == 1