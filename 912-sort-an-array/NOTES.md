```
# Bubble sort
# Time - O(N^2)
# Space - O(1)
class Solution:
def sortArray(self, nums: List[int]) -> List[int]:
for i in range(len(nums)-1):
for j in range(0, len(nums)-i-1):
if nums[j] > nums[j+1]:
nums[j], nums[j+1] = nums[j+1], nums[j]
return nums
```
​
```
# Selection Sort
# Time - O(N^2)
# Space - O(1)
class Solution:
def sortArray(self, nums: List[int]) -> List[int]:
for i in range(len(nums)):
minId = i
for j in range(i+1, len(nums)):
if nums[minId] > nums[j]:
minId = j
nums[minId], nums[i] = nums[i], nums[minId]
return nums
```