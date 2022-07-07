# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, maxSoFar):
        if not node:
            return
        
        if node.val >= maxSoFar:
            self.goodNodes.append(node.val)
            
        self.dfs(node.left, max(maxSoFar, node.val))
        self.dfs(node.right, max(maxSoFar, node.val))
        
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = []
        self.dfs(root, root.val)
        return len(self.goodNodes)