```
class Solution:
def mirrorReflection(self, p: int, q: int) -> int:
# Solution - Math GCD
# Time - O(logP)
# Space - O(1)
m = n = 1
while m * p != n * q:
n += 1
m = n * q // p
if n & 1 == 0:
return 2
elif m & 1 == 1:
return 1
else:
return 0
```