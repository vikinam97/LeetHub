```
class Solution:
def reorganizeString(self, s: str) -> str:
# Solution - greddy choose most frequent first
# Time - O(NlogN)
# Space - O(N)
charHash = [0] * 26
for char in s:
charHash[ord(char) - ord('a')] += 1
heap = []
for i in range(26):
if charHash[i] > 0:
heap.append((-1 * charHash[i], chr(ord('a') + i)))
heapq.heapify(heap)
result = []
while len(heap) >= 2:
chrA = heapq.heappop(heap)
chrB = heapq.heappop(heap)
result.append(chrA[1])
result.append(chrB[1])
if (-1 * chrA[0]) > 1:
heapq.heappush(heap, (chrA[0] + 1, chrA[1]))
if (-1 * chrB[0]) > 1:
heapq.heappush(heap, (chrB[0] + 1, chrB[1]))
if heap:
if heap[0][0] != -1:
return ""
result.append(heap[0][1])
return "".join(result)
```