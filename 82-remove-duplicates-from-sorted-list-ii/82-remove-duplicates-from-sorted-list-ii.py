# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rHead = ListNode("/")
        # temp.next = head
        # head = temp
        
        prev = rHead
        temp = head
        
        while temp:
                
            dup = False
            val = temp.val
            while temp.next and temp.next.val == val:
                temp = temp.next
                dup = True
            
            nxt = temp.next
            if dup == False:
                prev.next = temp
                prev = prev.next
                prev.next = None
                
            temp = nxt
            
        return rHead.next