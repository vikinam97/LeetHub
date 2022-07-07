```
class Solution:
def goodNodes(self, root: TreeNode) -> int:
# Solution - DFS traversal
# Time - O(N)
# Space - O(N)
self.goodNodes = 0
self.dfs(root, root.val)
return self.goodNodes
def dfs(self, node, maxSoFar):
if not node:
return
if node.val >= maxSoFar:
self.goodNodes += 1
self.dfs(node.left, max(maxSoFar, node.val))
self.dfs(node.right, max(maxSoFar, node.val))
```