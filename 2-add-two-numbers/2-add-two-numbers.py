# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(None)
        ptr = result
        carry = 0
        while l1 != None or l2 != None or carry:
            l1v, l2v = 0,0
            if l1:
                l1v = l1.val
            if l2:
                l2v = l2.val
            
            add = l1v + l2v + carry
            
            if add >= 10:
                carry = 1
                ptr.next = ListNode(add-10)
            else:
                ptr.next = ListNode(add)
                carry = 0
            
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
            ptr = ptr.next
            
        return result.next 
        