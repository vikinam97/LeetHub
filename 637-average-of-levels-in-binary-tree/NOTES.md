```
class Solution:
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
# Solution - level order traversal
# Time - O(N)
# Space - O(N)
bfs = [root]
result = []
while bfs:
sm, nxt = 0, []
for node in bfs:
sm += node.val
if node.left: nxt.append(node.left)
if node.right: nxt.append(node.right)
result.append(sm / len(bfs))
bfs = nxt
return result
```