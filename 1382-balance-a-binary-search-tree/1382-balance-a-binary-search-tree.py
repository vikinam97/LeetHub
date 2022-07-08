# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, preorder):
        if not node: 
            return
        
        self.dfs(node.left, preorder)
        preorder.append(node)
        self.dfs(node.right, preorder)
        
    def genTree(self, preorder):
        if not preorder:
            return None
        
        mid = len(preorder) // 2
        node = preorder[mid]
        
        node.left = self.genTree(preorder[:mid])
        node.right = self.genTree(preorder[mid+1:])
        
        return node
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        preorder = []
        self.dfs(root, preorder)
        
        return self.genTree(preorder)
        
        