"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        bfs, result = [root], []
        
        while bfs:
            nxt, level = [], []
            
            for node in bfs:
                level.append(node.val)
                for child in node.children:
                    nxt.append(child)
            
            bfs = nxt
            result.append(level)
        
        return result