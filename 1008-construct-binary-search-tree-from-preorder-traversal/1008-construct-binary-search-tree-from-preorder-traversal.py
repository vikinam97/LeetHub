# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, preorder, mn, mx):
        if self.cur >= len(preorder) or not (mn < preorder[self.cur] < mx):
            return None
        
        curVal = preorder[self.cur]
        node = TreeNode(curVal)
        self.cur += 1
        node.left = self.dfs(preorder, mn, curVal)
        node.right = self.dfs(preorder, curVal, mx)
        
        return node
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.cur = 0
        return self.dfs(preorder, float('-inf'), float('inf'))