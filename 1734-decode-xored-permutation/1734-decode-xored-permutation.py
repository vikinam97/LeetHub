class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        
        def findXorN(n):
            rem = n % 4
            
            if rem == 1:
                return 1
            
            if rem == 2:
                return n + 1
            
            if rem == 3:
                return 0
            
            return n
                
        
        xorN = findXorN(len(encoded) + 1)
        
        xorOfEven = encoded[0]
        i = 2
        while i < len(encoded):
            xorOfEven = xorOfEven ^ encoded[i]
            i += 2
            
        lastNumber = xorOfEven ^ xorN;
        
        result = [0] * (len(encoded) + 1)
        
        result[len(encoded)] = lastNumber
        
        i = len(encoded) - 1
        
        while i >= 0:
            result[i] = encoded[i] ^ result[i+1]
            i -= 1
        
        return result;
            