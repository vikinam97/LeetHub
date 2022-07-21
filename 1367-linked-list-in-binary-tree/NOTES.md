# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
# Solution - traversal
# Time - O(N * M)
#     N - no of tree nodes
#     M - no of list nodes
# Space - O(max(N, M))
return self.dfs(root, head)
def checkcontinuous(self, tNode, lNode):
if not tNode and not lNode:
return True
if not tNode:
return False
if not lNode:
return True
if tNode.val != lNode.val:
return False
return self.checkcontinuous(tNode.left, lNode.next) or self.checkcontinuous(tNode.right, lNode.next)
def dfs(self, tNode, head):
if not tNode:
return False
if tNode.val == head.val and self.checkcontinuous(tNode, head):
return True
return self.dfs(tNode.left, head) or self.dfs(tNode.right, head)
```