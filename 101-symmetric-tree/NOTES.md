return False
bfs = nxtLevel
return True
​
class Solution1:
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
# Solution - traversal recursive
# Time - O(N)
# Space - (N) recursice stack
if not root:
return True
return self.traverse(root.left, root.right)
def traverse(self, left, right):
if not left and not right:
return True
if (not left and right) or (left and not right) or left.val != right.val:
return False
return self.traverse(left.left, right.right) and self.traverse(left.right, right.left)
```