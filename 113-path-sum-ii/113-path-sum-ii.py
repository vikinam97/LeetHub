# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recur(self, node, path, sm, target):
        if not node: 
            return
        
        if not node.left and not node.right:
            if sm+node.val == target:
                self.paths.append(path[:] + [node.val])
            return
        
        path.append(node.val)
        self.recur(node.left, path, sm + node.val, target)
        self.recur(node.right, path, sm + node.val, target)
        path.pop()
    
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.paths = []
        self.recur(root, [], 0, targetSum)
        return self.paths
        