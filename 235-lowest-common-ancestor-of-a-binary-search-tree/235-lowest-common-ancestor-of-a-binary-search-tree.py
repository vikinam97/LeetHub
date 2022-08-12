# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, node, p, q):
        if not node: 
            return
        
        if node == p or node == q:
            return node
        
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right, p, q)
        
        return node if l and r else l or r
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)