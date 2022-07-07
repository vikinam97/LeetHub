```
class Solution:
def flatten(self, root: Optional[TreeNode]) -> None:
# Solution - using save preorder and re connect
# Time - O(N)
# Space - O(N)
if not root:
return []
self.preorder = []
self.dfs(root)
head = self.preorder[0]
for i in range(len(self.preorder)-1):
node = self.preorder[i]
node.left = None
node.right = self.preorder[i+1]
self.preorder[-1].right = None
self.preorder[-1].left = None
return head
​
def dfs(self, node):
if not node:
return
self.preorder.append(node)
self.dfs(node.left)
self.dfs(node.right)
```