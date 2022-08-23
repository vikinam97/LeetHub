# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self, head):
        prev = None
        nxt = None
        while head:
            cur = head
            nxt = head.next
            
            cur.next = prev
            prev = cur
            head = nxt
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head.next:
            return True
        
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow            
            slow = slow.next
        
        fPart = sPart = None
        if fast:
            fPart = head
            sPart = slow.next
            prev.next = None
        else:
            fPart = head
            sPart = slow
            prev.next = None
        sPart = self.reverse(sPart)

        
        while fPart and sPart:
            if sPart.val != fPart.val:
                return False
            sPart = sPart.next
            fPart = fPart.next
        
        return not fPart and not sPart
        
        
