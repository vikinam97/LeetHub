# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                
        slow, fast = head, head
        prev = None
        while fast and n:
            n -= 1
            fast = fast.next
        
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev == None:
            return head.next
        
        prev.next = prev.next.next
        
        return head
        