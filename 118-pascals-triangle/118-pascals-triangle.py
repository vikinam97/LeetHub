class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resultArr = []
        
        resultArr.append([1])
        
        for row in range(1, numRows):
            newRow = [0] * (row + 1)
            resultArr.append(newRow)
            
            newRow[0] = 1
            newRow[row] = 1
            
            for col in range(1, row):
                resultArr[row][col] = resultArr[row-1][col-1] + resultArr[row-1][col]
            
        return resultArr
                    
        