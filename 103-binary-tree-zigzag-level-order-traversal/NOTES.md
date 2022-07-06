```
class Solution:
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# Solution - traversal
# Time - O(N)
# Space - O(N)
if not root:
return []
bfs = [root]
di = 0
result = []
while bfs:
nxtLevel = []
lvl = []
for node in bfs:
lvl.append(node.val)
if node.left:
nxtLevel.append(node.left)
if node.right:
nxtLevel.append(node.right)
if di == 1:
lvl.reverse()
result.append(lvl)
di = 1 if di == 0 else 0
bfs = nxtLevel
return result
```