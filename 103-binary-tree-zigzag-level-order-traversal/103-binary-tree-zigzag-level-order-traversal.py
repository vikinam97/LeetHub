# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        bfs = [root]
        
        di = 0
        result = []
        while bfs:
            nxtLevel = []
            lvl = []
            for node in bfs:
                lvl.append(node.val)
                if node.left: 
                    nxtLevel.append(node.left)
                if node.right:
                    nxtLevel.append(node.right)
            
            if di == 1:
                lvl.reverse()
            
            result.append(lvl)
            di = 1 if di == 0 else 0
            bfs = nxtLevel
        return result
                
                    
                    
        