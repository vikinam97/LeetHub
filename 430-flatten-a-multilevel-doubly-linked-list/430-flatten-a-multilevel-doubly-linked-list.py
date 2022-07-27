class Solution:
    
    def recur(self, levelHead):
        if not levelHead:
            return
        
        temp = levelHead
        while temp:
            
            self.current.next = temp
            temp.prev = self.current
            self.current = self.current.next
            
            next = temp.next
            child = temp.child
            temp.child = None
            
            if child:
                self.recur(child)
                
            temp = next
        
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return  head
        
        self.current = Node("/", None, None, None)
        self.recur(head)
        head.prev = None
        
        return head

        
        
        
        

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
