class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        for i in range(32):
            if a == 0 and b == 0 and c == 0:
                break
                
            aBit = a & 1
            bBit = b & 1
            cBit = c & 1
            
            if cBit == 1:
                if aBit == 0 and bBit == 0:
                    count += 1
            else:
                if aBit == 1:
                    count += 1
                if bBit == 1:
                    count += 1
            
            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        return count