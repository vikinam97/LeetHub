```
class Solution:
def isPowerOfFour(self, n: int) -> bool:
# Solution - Without loops
# Time - O(logN)
# Space - O(1)
if n < 1:
return False
log = math.log(n, 4)
return int(log) == log
```
```
class Solution1:
def isPowerOfFour(self, n: int) -> bool:
# Solution - finding the log
# Time - O(logN)
# Space - O(1)
while n >= 4:
n = n / 4
if n != int(n): return False
n = int(n)
return n == 1
```