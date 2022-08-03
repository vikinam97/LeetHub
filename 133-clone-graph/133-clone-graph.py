"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def dfsClone(self, node, seenSet):
        if not node: 
            return None
        
        if node.val in seenSet:
            return seenSet[node.val]
        
        clone = Node(node.val)
        seenSet[node.val] = clone
        
        for n in node.neighbors: 
            clone.neighbors.append(self.dfsClone(n, seenSet))
        
        return clone
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfsClone(node, {})