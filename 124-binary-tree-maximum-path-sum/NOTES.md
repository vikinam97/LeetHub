```
class Solution:
def maxPathSum(self, root: Optional[TreeNode]) -> int:
# Solution - traversal
# Time - O(N)
# Space - O(N) for skew tree
self.max = float('-inf')
self.traverse(root)
return self.max
def traverse(self, node):
if not node:
return 0
left = self.traverse(node.left)
right = self.traverse(node.right)
# considering
#     left + cur
#     right + cur
#     cur
#     left + cur + right
self.max = max(self.max, node.val, left + node.val, right + node.val, left + right + node.val )
return max(left + node.val, right + node.val, node.val)
```