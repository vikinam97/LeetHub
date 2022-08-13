```
class Solution:
def leastInterval(self, tasks: List[str], n: int) -> int:
# Solution - greedy - rearrage distant apart technique
# Time - O(NlogN)
# Space - O(26) -> O(1)
taskFreq = Counter(tasks)
heap = [(-1*taskFreq[task], task) for task in taskFreq]
heapq.heapify(heap)
time = 0
while heap:
i = 0
pushBack = []
while heap and i <= n:
count, task = heapq.heappop(heap)
if count + 1 < 0:
pushBack.append((count+1, task))
i += 1
time += ( n+1 if pushBack else i)
while pushBack:
heapq.heappush(heap, pushBack.pop())
return time
```