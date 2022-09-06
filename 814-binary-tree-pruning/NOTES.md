```
​
class Solution:
def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# Solution - DFS traversal
# Time - O(N)
# Space - O(N)
v = self.recur(root)
if not v and not root.val:
return None
return root
def recur(self, node):
if not node: return
l = self.recur(node.left)
if not l:
node.left = None
r = self.recur(node.right)
if not r:
node.right = None
return node.val or l or r
```