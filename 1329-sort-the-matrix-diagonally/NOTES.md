```
class Solution:
def diagonalSort(self, A):
# Solution - get vales, sort and put back
# Time - O(NlogN)
# Space - O(1)
n, m = len(A), len(A[0])
d = collections.defaultdict(list)
for i in range(n):
for j in range(m):
d[i - j].append(A[i][j])
for k in d:
d[k].sort(reverse=1)
for i in range(n):
for j in range(m):
A[i][j] = d[i - j].pop()
return A
```