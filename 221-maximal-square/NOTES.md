```
class Solution:
def maximalSquare(self, matrix: List[List[str]]) -> int:
# Solution - DP - Space Optimized - Tabulation
# Time - O(N*N)
# Space - O(N)
h, w = len(matrix), len(matrix[0])
pdp = [0] * w
maxSoFar = 0
for i in range(0, h):
cdp = [0] * w
for j in range(0, w):
if i == 0:
cdp[j] = int(matrix[0][j])
elif j == 0:
cdp[0] = int(matrix[i][0])
elif matrix[i][j] == "1":
cdp[j] = min(pdp[j], cdp[j-1], pdp[j-1]) + 1
maxSoFar = max(maxSoFar, cdp[j] * cdp[j])
pdp = cdp
return maxSoFar
```
```
class Solutio1:
def maximalSquare(self, matrix: List[List[str]]) -> int:
# Solution - DP - Tabulation
# Time - O(N*N)
# Space - O(N*N)
h, w = len(matrix), len(matrix[0])
dp = [[0]*w for _ in range(h)]
maxSoFar = 0
for i in range(0, h):
for j in range(0, w):
if i == 0:
dp[0][j] = int(matrix[0][j])
elif j == 0:
dp[i][0] = int(matrix[i][0])
elif matrix[i][j] == "1":