class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rView = []
        seenMap = {}
        def dfs(node, lvl):
            if not node: 
                return
            
            if lvl not in seenMap:
                seenMap[lvl] = 1
                rView.append(node.val)
            
            dfs(node.right, lvl+1)
            dfs(node.left, lvl+1)
            
        dfs(root, 0)
        return rView
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Solution - BFS
        # Time - O(N)
        # Space - O(N)
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
        
        
        
        
        