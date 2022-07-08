```
class Solution:
def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
# Solution - BST property
# Time - O(N)
# Space - O(N)
self.cur = 0
return self.dfs(preorder, float('-inf'), float('inf'))
def dfs(self, preorder, mn, mx):
if self.cur >= len(preorder) or not (mn < preorder[self.cur] < mx):
return None
curVal = preorder[self.cur]
node = TreeNode(curVal)
self.cur += 1
node.left = self.dfs(preorder, mn, curVal)
node.right = self.dfs(preorder, curVal, mx)
return node
```