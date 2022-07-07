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

        self.preorder.append(node)
        self.dfs(node.left)
        self.dfs(node.right)
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return []
        self.preorder = []
        self.dfs(root)
        head = self.preorder[0]
        for i in range(len(self.preorder)-1):
            node = self.preorder[i]
            node.left = None
            node.right = self.preorder[i+1]
        self.preorder[-1].right = None        
        self.preorder[-1].left = None
        
        return head

        
        
        