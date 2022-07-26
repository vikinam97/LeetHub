```
class Solution:
def traverse(self, node, p, q):
if not node:
return 0
if node == p or node == q:
return node
l = self.traverse(node.left, p, q)
r = self.traverse(node.right, p, q)
return node if l and r else l or r
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
# Solution - traversal | meeting node
# Time - O(N)
# Space - O(N)
return self.traverse(root, p, q)
```
​
```
class Solution:
def traverse(self, node, p, q, curPath):
if not node:
return
if node == p or node == q:
self.paths.append(curPath + [node])
self.traverse(node.left, p, q, curPath + [node])
self.traverse(node.right, p, q, curPath + [node])