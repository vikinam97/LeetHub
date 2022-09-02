# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        bfs = [root]
        result = []
        
        while bfs:
            sm, nxt = 0, []
            
            for node in bfs:
                sm += node.val
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            
            result.append(sm / len(bfs))
            bfs = nxt
        
        return result
        