```
from heapq import heapify, heappop, heappush
​
class Solution:
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
# Solution - Heap
# Time - O(NlogK)
# Space - O(K)
heap = []
i = 0
while i < k:
heap.append((-1*nums[i], i))
i += 1
heapify(heap)
winMax = [-1 * heap[0][0]]
while i < len(nums):
heappush(heap, (-1*nums[i], i))
while heap and heap[0][1] < i - k + 1:
heappop(heap)
winMax.append(-1 * heap[0][0])
i += 1
return winMax
```