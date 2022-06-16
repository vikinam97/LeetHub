```
class Solution:
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
minLen = float('Inf')
i, j = 0, 0
slidingSum = 0
while j < len(nums):
slidingSum += nums[j]
while slidingSum >= target:
slidingSum = slidingSum - nums[i]
if minLen > (j - i + 1):
print(i, j)
minLen = (j - i + 1)
i += 1
j += 1
return minLen if minLen != float('Inf') else 0
```