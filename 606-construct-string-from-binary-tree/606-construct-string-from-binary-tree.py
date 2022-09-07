# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recur(self, node):
        if not node: return
        
        result = []
        result.append(str(node.val))
        
        l = self.recur(node.left)
        r = self.recur(node.right)
        
        if l:
            result.append(f'({l})')
        
        if r != None:
            if not l:
                result.append(f'()')
            result.append(f'({r})')
        
        return "".join(result)
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        return self.recur(root)
        