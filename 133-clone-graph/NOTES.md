```
class Solution:
def cloneGraph(self, node: 'Node') -> 'Node':
# Solution - DFS
# Time - O(V+E)
# Space - O(V)
return self.dfsClone(node, {})
def dfsClone(self, node, seenSet):
if not node:
return None
if node.val in seenSet:
return seenSet[node.val]
clone = Node(node.val)
seenSet[node.val] = clone
for n in node.neighbors:
clone.neighbors.append(self.dfsClone(n, seenSet))
return clone
```