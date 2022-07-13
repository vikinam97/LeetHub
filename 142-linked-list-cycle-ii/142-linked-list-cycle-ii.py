# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first check cycle or not
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
    
class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution - Hash Map
        # Time - O(N)
        # Space - O(N)
        hashMap = {}
        while head:
            if head in hashMap:
                return head
            
            hashMap[head] = True
            head = head.next
        
        return None
        