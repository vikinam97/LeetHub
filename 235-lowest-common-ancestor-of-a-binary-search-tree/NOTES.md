```
class Solution:
def dfs(self, node, p, q):
if not node:
return
if (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
return node
return self.dfs(node.left, p, q) or self.dfs(node.right, p, q)
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
return self.dfs(root, p, q)
```
​