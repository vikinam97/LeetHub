```
class Solution:
def uniquePaths(self, m: int, n: int) -> int:
# Solution - dynamic programming | memoization
# Time - O(M * N)
# Space - O(M * N)
self.memo = {}
return self.recur(0, 0, m, n)
def recur(self, i, j, m, n):
if i > m or j > n:
return 0
if i == (m-1) and j == (n-1):
return 1
if (i, j) in self.memo:
return self.memo[(i, j)]
self.memo[(i, j)] = self.recur(i, j+1, m, n) + self.recur(i+1, j, m, n)
return self.memo[(i, j)]
```