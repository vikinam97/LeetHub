# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNode(self, node, dep, parent, x, y, nodes):
        if not node:
            return;
        
        if len(nodes) >= 2:
            return
        
        if node.val == x or node.val == y:
            nodes.append([node, parent, dep])
            
        self.findNode(node.left, dep + 1, node, x, y, nodes)
        self.findNode(node.right, dep + 1, node, x, y, nodes)        
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodes = []
        self.findNode(root, 0, None, x, y, nodes)
        
        if nodes[0][2] == nodes[1][2] and nodes[0][1] != nodes[1][1]:
            return True
        
        return False