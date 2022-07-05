# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        bfs = [[root, 1]]
        levelMap = {}
        result = []
        while bfs:
            nxtLevel = []
            for node, lvl in bfs:
                if lvl not in levelMap:
                    levelMap[lvl] = 1
                    result.append(node.val)
                
                if node.right:
                    nxtLevel.append([node.right, lvl + 1])
                if node.left:
                    nxtLevel.append([node.left, lvl + 1])
            
            bfs = nxtLevel
        
        return result
        
        
        
        
        