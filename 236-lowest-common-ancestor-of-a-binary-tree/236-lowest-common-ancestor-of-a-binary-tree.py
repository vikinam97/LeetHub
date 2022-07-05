# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, p, q, curPath):
        if not node:
            return
        
        if node == p or node == q:
            
            self.paths.append(curPath + [node])
        
        self.traverse(node.left, p, q, curPath + [node])
        self.traverse(node.right, p, q, curPath + [node])
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
            
        