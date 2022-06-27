```
class Solution:
def minPartitions(self, n: str) -> int:
# Solution - max digit number of values required
# Time - O(N) N = len of string
# Space - O(1)
return max(int(digit) for digit in n)
# maxSoFar = int(n[0])
# for num in n:
#     num = int(num)
#     maxSoFar = max(maxSoFar, num)
# return maxSoFar
```