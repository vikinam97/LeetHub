# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution - BFS + deque
        # Time - O(N)
        # Space - O(N)
        if not root:
            return []
        
        traversal = collections.deque([])
        
        bfs = [root]
        while bfs:
            nxtLvl = []
            lvl = []
            for node in bfs:
                lvl.append(node.val)
                
                if node.left: nxtLvl.append(node.left)
                if node.right: nxtLvl.append(node.right)
            
            bfs = nxtLvl
            traversal.appendleft(lvl)
        
        return traversal