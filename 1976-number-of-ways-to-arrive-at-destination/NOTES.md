```
​
MOD = (10**9) + 7
​
class Solution:
def countPaths(self, n: int, roads: List[List[int]]) -> int:
# Solution - Dijstra
# Time - O(RlogN)
#     - R = len(roads)
#     - N = n
# Space - O(N)
adjMat = defaultdict(list)
for u, v, t in roads:
adjMat[u].append((v, t))
adjMat[v].append((u, t))
times = [float('inf')] * n
times[0] = 0
ways = [0] * n
ways[0] = 1
heap = [(0, 0)] # (time, vertex)
while heap:
distance, node = heapq.heappop(heap)
for adj, dv in adjMat[node]:
if dv + distance < times[adj]:
times[adj] = dv + distance
heapq.heappush(heap, (dv + distance, adj))
ways[adj] = ways[node]
elif times[adj] == dv + distance:
ways[adj] += ways[node]
​
return ways[n-1] % MOD
```