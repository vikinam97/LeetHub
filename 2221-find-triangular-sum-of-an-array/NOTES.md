```
class Solution:
def triangularSum(self, nums: List[int]) -> int:
# Solution - process simulation
# Time - O(N^2)
# Space - O(N)
while len(nums) > 1:
new = []
for i in range(len(nums)-1):
new.append((nums[i] + nums[i+1]) % 10)
nums = new
return nums[0]
```