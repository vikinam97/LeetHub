```
class Solution:
def longestConsecutive(self, nums: List[int]) -> int:
# Solution - Hash map and consecutive traversal
# Time - O(N)
# Space - O(N)
hashMap = {}
for num in nums:
hashMap[num] = 1
seen = {}
maxSoFar = 0
for num in nums:
if num in seen:
continue
seen[num] = 1
count = 1
# traverse left
left = num - 1
while left in hashMap:
seen[left] = 1
count += 1
left -= 1
# traverse right
right = num + 1
while right in hashMap:
seen[right] = 1
count += 1
right += 1
maxSoFar = max(maxSoFar, count)
return maxSoFar
```