# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recur(self, node):
        if not node:
            return
        
        self.recur(node.left)
        self.traversal.append(node.val)
        self.recur(node.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal = []
        self.recur(root)
        return self.traversal