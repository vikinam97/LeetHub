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
        
        if (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
            return node
        
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right, p, q)
        
        return l or r
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
