```
class Solution:
def levelOrder(self, root: 'Node') -> List[List[int]]:
# Solution - BFS
# Time - O(V+E)
# Space - O(V)
if not root:
return []
bfs, result = [root], []
while bfs:
nxt, level = [], []
for node in bfs:
level.append(node.val)
for child in node.children:
nxt.append(child)
bfs = nxt
result.append(level)
return result
```