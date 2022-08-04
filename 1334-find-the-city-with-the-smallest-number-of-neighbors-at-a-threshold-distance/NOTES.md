```
class Solution:
def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
# Solution - Floyd Warshal
# Time - O(V^3)
# Space - O(V^2)
grid = [[float('inf')] * n for i in range(n)]
for i in range(n):
grid[i][i] = 0
for a, b, wt in edges:
grid[a][b] = grid[b][a] = wt
for pivot in range(n):
for i in range(n):
for j in range(n):
if i == pivot or j == pivot or i == j:
continue
grid[i][j] = min(grid[i][j], grid[i][pivot] + grid[pivot][j])
minCityCount, minCity = float('inf'), float('-inf')
for i in range(n):
count = 0
for j in range(n):
if grid[i][j] <= distanceThreshold:
count += 1
if minCityCount >= count:
minCityCount = count
minCity = max(minCity, i)
return minCity
```