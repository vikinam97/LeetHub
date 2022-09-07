```
class Solution:
def tree2str(self, root: Optional[TreeNode]) -> str:
# Solution - DFS
# Time - O(N)
# Space - O(N)
return self.recur(root)
def recur(self, node):
if not node: return
result = []
result.append(str(node.val))
l = self.recur(node.left)
r = self.recur(node.right)
if l:
result.append(f'({l})')
if r != None:
if not l:
result.append(f'()')
result.append(f'({r})')
return "".join(result)
```