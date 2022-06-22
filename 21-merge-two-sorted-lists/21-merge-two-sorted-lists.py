# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = list1
        j = list2
        
        head = ListNode(0)
        temp = head
        
        while i != None and j != None:
            if i.val < j.val:
                temp.next = i
                i = i.next
            else:
                temp.next = j
                j = j.next
            
            temp = temp.next
        
        while i != None:
            temp.next = i
            temp = temp.next
            i = i.next
        
        while j != None:
            temp.next = j
            temp = temp.next
            j = j.next
            
        return head.next