```
class Solution:
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
# Solution - greedy .. took max profit from diffrence
# Time - O(NlogN)
# Space - O(N)
heap = []
for i in range(len(costs)):
a, b = costs[i]
heap.append((-1 * (b - a), a, b))
heapq.heapify(heap)
ASumCost = 0
for i in range(len(costs) // 2):
ele = heapq.heappop(heap)
ASumCost += ele[1]
BSumCost = 0
while heap:
ele = heapq.heappop(heap)
BSumCost += ele[2]
return ASumCost + BSumCost
```
​