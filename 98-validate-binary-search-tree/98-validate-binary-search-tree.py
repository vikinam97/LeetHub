# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, node, minRg, maxRg):
        if not node:
            return True
        
        if minRg >= node.val or node.val >= maxRg:
            return False
        
        return self.dfs(node.left, minRg, node.val) and self.dfs(node.right, node.val, maxRg)
        