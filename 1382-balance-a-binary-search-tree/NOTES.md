```
class Solution:
def balanceBST(self, root: TreeNode) -> TreeNode:
# Solution - sorted array in mid to form tree
# Time - O(N)
# Space - O(N)
preorder = []
self.dfs(root, preorder)
return self.genTree(preorder)
def dfs(self, node, preorder):
if not node:
return
self.dfs(node.left, preorder)
preorder.append(node)
self.dfs(node.right, preorder)
def genTree(self, preorder):
if not preorder:
return None
mid = len(preorder) // 2
node = preorder[mid]
node.left = self.genTree(preorder[:mid])
node.right = self.genTree(preorder[mid+1:])
return node
```