# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 0 un monitored
    # 1 monitored
    # 2 monitored and camera
    def traverse(self, node):
        if not node:
            return 1
        
        lSts = self.traverse(node.left)
        rSts = self.traverse(node.right)
        
        if lSts == 0 or rSts == 0:
            self.numCams += 1
            return 2
        
        if lSts == 2 or rSts == 2:
            return 1
        
        return 0
    
    def minCameraCover(self, root: TreeNode) -> int:
        self.numCams = 0
        
        rootSts = self.traverse(root)
        print(rootSts)
        
        if rootSts == 0:
            self.numCams += 1
            
        return self.numCams