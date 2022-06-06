class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        # solution 1         
        while x != y:
            if (x & 1) != (y & 1):
                count += 1;
            x = x >> 1
            y = y >> 1
            
        # solution 2 
        # x = x ^ y
        # while x != 0:
        #     count += 1
        #     x = x & (x-1)
            
        return count