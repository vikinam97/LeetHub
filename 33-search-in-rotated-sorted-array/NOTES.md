```
class Solution:
# Solution - binary srearch
# Time - O(log (N))
# Space - O(1)
def search(self, nums: List[int], target: int) -> int:
return self.binary_search(nums, 0, len(nums)-1, target)
def binary_search(self, nums, start, end, target):
if start > end:
return -1
mid = (start+end)//2
if nums[mid] == target:
return mid
# start to mid is sorted
if nums[start] <= nums[mid]:
if nums[start]<=target<nums[mid]:
return self.binary_search(nums, start, mid-1, target)
else:
return self.binary_search(nums, mid+1, end, target)
# mid to end is sorted
else:
if nums[mid]<target<=nums[end]: