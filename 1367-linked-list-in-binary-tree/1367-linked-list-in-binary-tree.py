# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkcontinuous(self, tNode, lNode):
        if not tNode and not lNode:
            return True
        
        if not tNode:
            return False
        
        if not lNode:
            return True
        
        if tNode.val != lNode.val:
            return False
        
        return self.checkcontinuous(tNode.left, lNode.next) or self.checkcontinuous(tNode.right, lNode.next)
    
    def dfs(self, tNode, lNode):
        if not tNode and not lNode:
            return True
        
        if not tNode:
            return False
        
        if not lNode:
            return True
        
        if tNode.val == lNode.val and self.checkcontinuous(tNode, lNode):
            return True
        
        return self.dfs(tNode.left, lNode) or self.dfs(tNode.right, lNode)
        
    
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.dfs(root, head)