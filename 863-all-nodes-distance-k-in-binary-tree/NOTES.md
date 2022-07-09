```
class Solution:
def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
# Solution  - BFS with parent
# Time - O(N)
# Space - O(N)
self.parents = {}
self.dfs(root)
seen = {}
bfs = [target]
i = 0
while bfs and i < k:
nxtLevel = []
for node in bfs:
seen[node.val] = 1
if node.left and node.left.val not in seen:
nxtLevel.append(node.left)
if node.right and node.right.val not in seen:
nxtLevel.append(node.right)
if node.val in self.parents and self.parents[node.val].val not in seen:
nxtLevel.append(self.parents[node.val])
bfs = nxtLevel
i += 1
result = []
for node in bfs:
result.append(node.val)
return result
def dfs(self, node, parent=None):
if not node:
return None
if parent != None:
self.parents[node.val] = parent
self.dfs(node.left, node)
self.dfs(node.right, node)
```