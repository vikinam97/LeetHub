return mergeSortedArray(left, right)
return partition(nums)
def bubbleSort(self, nums):
# Bubble sort
# Time - O(N^2)
# Space - O(1)
for i in range(len(nums)-1):
for j in range(0, len(nums)-i-1):
if nums[j] > nums[j+1]:
nums[j], nums[j+1] = nums[j+1], nums[j]
return nums
def selectionSort(self, nums):
# Selection Sort
# Time - O(N^2)
# Space - O(1)
for i in range(len(nums)):
minId = i
for j in range(i+1, len(nums)):
if nums[minId] > nums[j]:
minId = j
nums[minId], nums[i] = nums[i], nums[minId]
return nums
```