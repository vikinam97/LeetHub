```
class Solution:
def generate(self, numRows: int) -> List[List[int]]:
# Time O(N * 2)
# Space O(N ^ 2)
resultArr = []
resultArr.append([1])
for row in range(1, numRows):
resultArr.append([0] * (row + 1))
# init first and last as 1
newRow[0] = 1
newRow[row] = 1
for col in range(1, row):
resultArr[row][col] = resultArr[row-1][col-1] + resultArr[row-1][col]
# if to calculate nCr then return
# resultArr[n][r]
return resultArr
```