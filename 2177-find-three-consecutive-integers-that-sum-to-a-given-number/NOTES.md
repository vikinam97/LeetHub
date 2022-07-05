```
class Solution:
def sumOfThree(self, num: int) -> List[int]:
# Solution - Math intution
# Time  - O(1)
# Space - O(1)
x = num // 3
if ((3 * x)) == num:
return [(x-1), x, (x+1)]
return []
```