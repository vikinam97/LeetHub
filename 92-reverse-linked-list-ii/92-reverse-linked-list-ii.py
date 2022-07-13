# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        flag = False
        node = head
        
        prev = None
        leftPrev = None
        rightNext = None
        
        leftNode = None
        rightNode = None
        i = 1
        while node:
            if i == left:
                leftNode = node
                leftPrev = prev
                flag = True
                
            nxt = node.next
            
            if i == right or not node.next:
                rightNode = node
                rightNext = nxt
                flag = False
                break
            
            prev = node
            node = nxt
            i += 1
        
        if not leftNode:
            return head
        
#         print(leftPrev)
#         print(leftNode)
        
#         print(rightNext)
#         print(rightNode)
        node = leftNode
        prev = None
        while node != rightNext:
            nxt = node.next
            
            node.next = prev
            
            prev = node
            node = nxt
        
        if leftPrev:
            leftPrev.next = prev
            prev = head    
            
        if leftNode:
            leftNode.next = rightNext
            
        return prev
            