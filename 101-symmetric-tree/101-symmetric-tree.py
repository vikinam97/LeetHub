class Solution:    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Solution - BFS
        # Time - O(N)
        # Space - O(N)
        if not root:
            return True
        bfs = [root]
        while bfs:
            nxtLevel = []
            lvl = []
            for node in bfs:
                if node: 
                    lvl.append(node.val)
                    nxtLevel.append(node.left)
                    nxtLevel.append(node.right)
                else:
                    lvl.append("")
            
            for i in range(len(lvl) // 2):
                if lvl[i] != lvl[(len(lvl)-1) - i]:
                    return False
                
            bfs = nxtLevel
        return True

class Solution1:    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Solution - traversal recursive
        # Time - O(N)
        # Space - (N) recursice stack
        
        if not root:
            return True
        
        return self.traverse(root.left, root.right)
    
    def traverse(self, left, right):
        if not left and not right:
            return True
        
        if (not left and right) or (left and not right) or left.val != right.val:
            return False
        
        return self.traverse(left.left, right.right) and self.traverse(left.right, right.left)