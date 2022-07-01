class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (-x[1]))
        
        curSize = 0
        total = 0
        for number, units in boxTypes:
            if curSize >= truckSize:
                break
            
            avail = truckSize - curSize
            
            if avail >= number:
                total += (number * units)
                curSize += number
            else:
                total += (avail * units)
                curSize += avail
        
        return total
            
        