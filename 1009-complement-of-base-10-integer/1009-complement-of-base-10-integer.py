class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        result = 0
        mask = 1 
        while n != 0:
            if n & 1 == 0:
                result = result | mask
            n = n >> 1
            mask = mask << 1
            
        return result
                