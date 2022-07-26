class Solution:
    def traverse(self, node, p, q):
        if not node:
            return 0
        
        if node == p or node == q:
            return node
        
        l = self.traverse(node.left, p, q)
        r = self.traverse(node.right, p, q)
        
        return node if l and r else l or r
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traverse(root, p, q)


class Solution1:
    def traverse(self, node, p, q, curPath):
        if not node:
            return
        
        if node == p or node == q:
            
            self.paths.append(curPath + [node])
        
        self.traverse(node.left, p, q, curPath + [node])
        self.traverse(node.right, p, q, curPath + [node])
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Solution - in order traversal and common
        # Time - O(N)
        # Space - O(N)
        
        self.paths = []
        self.traverse(root, p, q, [])
        path1 = self.paths[0]
        path2 = self.paths[1]
        path2.reverse()
        path1Hash = {}
        for i in range(len(path1)):
            path1Hash[path1[i].val] = 1
        
        for i in range(len(path2)):
            if path2[i].val in path1Hash:
                return path2[i]
        
        return None