class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        o1 = 0b00000000
        o2 = 0b11000000
        o3 = 0b11100000
        o4 = 0b11110000
        
        trail = 0b10000000
        
        def checkTrail(byte):
            return (byte & trail) == trail
        
        def getTrailLength(byte):
            if ((byte & o4) == o4) and ((byte & (1 << 3)) == 0):
                return 3
            if (byte & o3) == o3 and ((byte & (1 << 4)) == 0):
                return 2
            if (byte & o2) == o2 and ((byte & (1 << 5)) == 0):
                return 1
            if ((byte & (1 << 7)) == 0):
                return 0
            
            return -1
        
        i = 0
        while i < len(data):
            trailLen = getTrailLength(data[i])
            
            if trailLen == -1:
                return False
            i += 1;
            
            print("trail => ", trailLen)
            
            while trailLen > 0:
                if i >= len(data) or checkTrail(data[i]) == False:
                    return False
                i += 1
                trailLen -= 1
            
        return True