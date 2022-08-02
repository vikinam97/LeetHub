```
class Solution:
def traverseSource(self, node, edges):
cur, dist = node, 0
distList = [-1] * len(edges)
while cur != -1 and distList[cur] == -1:
distList[cur] = dist
cur = edges[cur]
dist += 1
return distList
def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
# Solution - find ditance and check
# Time - O(N)
# Space - O(N)
visited = [0] * len(edges)
dist1 = self.traverseSource(node1, edges)
dist2 = self.traverseSource(node2, edges)
meetNode, minSoFar = -1, float('inf')
for i in range(len(edges)):
if dist1[i] == -1 or dist2[i] == -1:
continue
​
if minSoFar > max(dist1[i], dist2[i]):
meetNode = i
minSoFar = max(dist1[i], dist2[i])
return meetNode
```