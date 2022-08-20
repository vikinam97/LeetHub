continue
cost = float('-inf') + 1000
if i + 1 < h:
cost = dp[i+1][j]
if j + 1 < w:
cost = max(cost, dp[i][j+1])
dp[i][j] = min(0, cost + dungeon[i][j])
return abs(dp[0][0]) +1
```
```
class Solution:
def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
# Solution - Recusion + Memoization
# Time - O(N*M)
# Space - O(N*M)
self.memo = {}
cost = self.recur(0, 0, dungeon)
return abs(cost) + 1
def recur(self, i, j, dungeon):
h, w = len(dungeon), len(dungeon[0])
if i >= h or j >= w:
return float('-inf') + 1000
if (i, j) in self.memo:
return self.memo[(i, j)]
if i == h-1 and j == w-1:
return min(dungeon[i][j], 0)
cost = max(self.recur(i + 1, j, dungeon),
self.recur(i, j + 1, dungeon)) + dungeon[i][j]
self.memo[(i, j)] = min(cost, 0)
return self.memo[(i, j)]
```