```
class Solution:
def searchRange(self, nums: List[int], target: int) -> List[int]:
# Solution - binary search
# Time - O(logN + N)
# Space - O(1)
l, r = 0, len(nums)-1
foundAt = -1
while l<= r:
mid = l + ((r - l) // 2)
if nums[mid] == target:
foundAt = mid
break
elif nums[mid] > target:
r = mid - 1
else:
l = mid + 1
if foundAt == -1:
return [-1, -1]
l, r = foundAt, foundAt
while l > 0 and nums[l-1] == target:
l -= 1
while r < len(nums) -1 and nums[r+1] == target:
r += 1
return [l, r]
```