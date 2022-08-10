```
import collections
​
class Solution:
def minTaps(self, n: int, ranges: List[int]) -> int:
# Solution - Greedy choose the one with largest range for every stand
# Time - O(NlogN)
# Space - O(N)
rangeList = []
for i in range(n+1):
rangeList.append((i - ranges[i], i + ranges[i]))
rangeList.sort()
rangeList = collections.deque(rangeList)
start, count = 0, 0
​
while start < n:
end = start
while rangeList and rangeList[0][0] <= start:
end = max(end, rangeList.popleft()[1])
if start == end:
return -1
start = end
count += 1
return count
```