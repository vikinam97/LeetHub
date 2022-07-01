```
class Solution:
def findKthNumber(self, m: int, n: int, k: int) -> int:
# Solution - using binary search of mid value and finding length of array
# Time - O((M+N) * log(min - max))
# Space - O(1)
def getCountOfNumsLessEqual(m, n, val):
r = m - 1
c = 0
count = 0
while c < n and r >= 0:
if ((r+1) * (c+1)) <= val:
count += r + 1
c += 1
else:
r -= 1
return count
l = 1
r = m * n
pKval = -1
while l <= r:
mid = l + ((r - l) // 2)
count = getCountOfNumsLessEqual(m, n, mid)
if count >= k:
pKval = mid
r = mid - 1
else:
l = mid + 1
return pKval
```