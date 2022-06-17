```
class Solution:
def minAbsDifference(self, nums: List[int], goal: int) -> int:
# Solution - 2 set binary serach
# Time - O(2^(N/2) * log(2^(N/2))
# Space O(2^n)
def generateSubsetSumList(st, ed):
result = [0]
for i in range(st, ed+1):
prevLen = len(result)
for j in range(prevLen):
result.append(result[j] + nums[i])
return result
#         def searchBinary(arr, target):
#             l, r = 0, len(arr) - 1
#             while l < r:
#                 mid = (l + r) // 2
#                 if arr[mid] == target:
#                     return arr[mid]
#                 elif arr[mid] > target:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             return arr[l]
list1 = generateSubsetSumList(0, (len(nums)) // 2)
list2 = generateSubsetSumList((len(nums)) // 2 + 1, len(nums) - 1)
list2.sort()
closeSoFar = float('infinity')
result = float('infinity')