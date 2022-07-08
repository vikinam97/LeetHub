# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, preorder, inorder):
        if not inorder:
            return None
        
        idx = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[self.cur]:
                idx = i
                break
                
        if idx == -1: 
            return None
        
        node = TreeNode(inorder[i])
        self.cur += 1
                
        node.left = self.helper(preorder, inorder[:idx])
        node.right = self.helper(preorder, inorder[idx+1:])
        
        return node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.cur = 0
        
        return self.helper(preorder, inorder)
