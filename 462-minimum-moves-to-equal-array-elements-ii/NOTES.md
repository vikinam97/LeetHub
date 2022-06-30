```
class Solution:
def minMoves2(self, nums: List[int]) -> int:
# Solution - Median
# Time - O(NlogN)
# Space - O(1)
nums.sort()
median = nums[len(nums) // 2]
steps = 0
for i in range(len(nums)):
steps += abs(nums[i] - median)
return steps
```