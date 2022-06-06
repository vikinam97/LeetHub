Time -> O(n)
space -> O(1)
```
class Solution:
def singleNumber(self, nums: List[int]) -> int:
xorResult = nums[0]
for i in range(1, len(nums)):
xorResult = xorResult^nums[i]
return xorResult;
```