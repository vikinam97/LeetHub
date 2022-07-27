# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:    
    
    def dfs(self, node):
        if not node:
            return 
        if not node.left and not node.right:
            return node
        
        left = node.left
        right = node.right
        
        lTree = self.dfs(node.left)
        rTree = self.dfs(node.right)
        
          
        if lTree:
            lTree.right = right
        node.left = None
        node.right = left or right
        
        return rTree or lTree or node
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        # Solution - traversal
        # Time - O(N)
        # Space - O(N)
        
        self.dfs(root)
        return root
        
        