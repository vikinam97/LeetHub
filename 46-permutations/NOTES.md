```
class Solution:
def permute(self, nums: List[int]) -> List[List[int]]:
# Solution - all combo
# Time - O(N!)
# Space - O(N!)
self.perList = []
self.recur(nums, [], set())
return self.perList
def recur(self, nums, path, used):
if len(path) == len(nums):
self.perList.append(path[:])
return
for num in nums:
if num not in used:
used.add(num)
path.append(num)
self.recur(nums, path, used)
path.pop()
used.remove(num)
```