# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return 0
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        
        self.max = max(self.max, node.val, left + node.val, right + node.val, left + right + node.val )
        
        return max(left + node.val, right + node.val, node.val)
        
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float('-inf')
        self.traverse(root)
        return self.max