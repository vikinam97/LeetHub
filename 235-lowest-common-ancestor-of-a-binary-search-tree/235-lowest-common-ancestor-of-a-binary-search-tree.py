# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Solution - bst traversal.
        # Time - O(N)
        # pace - O(1)
        
        pVal, qVal, node = p.val, q.val, root
        while node:
            nVal = node.val
            if nVal < pVal and nVal < qVal:
                node = node.right
            elif nVal > pVal and nVal > qVal:
                node = node.left
            else:
                return node

class Solution1:
    def dfs(self, node, p, q):
        if not node: 
            return
        
        if (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
            return node
        
        return self.dfs(node.left, p, q) or self.dfs(node.right, p, q)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Solution - bst traversal.
        # Time - O(N)
        # pace - O(N)
        
        return self.dfs(root, p, q)
