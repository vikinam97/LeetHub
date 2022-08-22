class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n < 1:
            return False
        log = math.log(n, 4)
        return int(log) == log
        
#         while n >= 4:
#             n = n / 4
#             if n != int(n): return False
#             n = int(n)
            
#         return n == 1