# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lHead = ListNode("/")
        gHead = ListNode('/')
        
        temp = head
        lNode = lHead
        gNode = gHead
        while temp:
            if temp.val < x:
                lNode.next = temp
                lNode = lNode.next
            else:
                gNode.next = temp
                gNode = gNode.next
            
            temp = temp.next
        
        lNode.next = gHead.next
        gNode.next = None
        
        return lHead.next