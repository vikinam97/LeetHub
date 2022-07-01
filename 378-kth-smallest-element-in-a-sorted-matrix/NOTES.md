```
class Solution:
def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
# Solution - using binary search of mid value and finding length of array
# Time - O((M+N) * log(min - max))
# Space - O(1)
def getCountOfNumsLessEqual(self, matrix, val):
r = len(matrix) - 1
c = 0
count = 0
while c < len(matrix[0]) and r >= 0:
if matrix[r][c] <= val:
count += r + 1
c += 1
else:
r -= 1
return count
l = matrix[0][0]
r = matrix[len(matrix)-1][len(matrix[0]) - 1]
pKval = -1
while l <= r:
mid = l + ((r - l) // 2)
count = self.getCountOfNumsLessEqual(matrix, mid)
if count >= k:
pKval = mid
r = mid - 1
else:
l = mid + 1
return pKval
# Solution - Max Heap
# Time - O(N^2)
# Space - O(K)
# heap = []
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         heapq.heappush(heap, -1 * matrix[i][j])
#         if len(heap) > k:
#             heapq.heappop(heap)
# return -1 * heap[0]
```