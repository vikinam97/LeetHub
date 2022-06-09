class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n != 0:
            pLsb = n & 1
            n = n >> 1
            print(pLsb, bin(n))
            if (n & 1) == pLsb:
                return False
        return True
                
#         c1 = 0b0101010101010101010101010101010
#         c2 = 0b1010101010101010101010101010101
        
#         return ((c1 & n) == n) or ((c2 & n) == n)
