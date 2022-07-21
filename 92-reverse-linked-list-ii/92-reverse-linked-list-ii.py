# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Solution - 1st find node and then reverse
        # Time - O(N)
        # Space - O(1)
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
        
        # if left position is not found
        if not leftNode:
            return head
        
        node = leftNode
        prev = None
        while node != rightNext:
            nxt = node.next
            
            node.next = prev
            
            prev = node
            node = nxt
        
        # if left is not the 1st node
        if leftPrev:
            leftPrev.next = prev
            prev = head    
            
        # if right is not the last node
        if leftNode:
            leftNode.next = rightNext
            
        return prev
            