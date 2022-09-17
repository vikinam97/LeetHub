```
class Solution:
def calcDistance(self, point1, point2):
return math.dist(point1, point2)
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
# Solution - Heap
# Time - O(KlogN + N)
# Space - O(N)
heap = []
for point in points:
dist = self.calcDistance([0, 0], point)
heap.append((dist, point))
heapq.heapify(heap)
result = []
while len(result) < k and heap:
result.append(heapq.heappop(heap)[1])
return result
```