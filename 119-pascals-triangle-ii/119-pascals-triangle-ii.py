class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        
        for i in range(1, rowIndex+1):
            row = [0] * (i + 1)
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row) - 1):
                row[j] = prev[j] + prev[j-1]
            
            prev = row
        
        return prev
                
            