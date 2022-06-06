Time O(log n)
Space O(1)
```
class Solution:
def hammingDistance(self, x: int, y: int) -> int:
count = 0
while x != y:
if (x & 1) != (y & 1):
count += 1;
x = x >> 1
y = y >> 1
return count
```