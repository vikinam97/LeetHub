# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, list):
        count = 0
        while list != None:
            count+=1;
            list = list.next;
        return count;
    
    def moveStep(self, list, step):
        while step > 0:
            list = list.next
            step -= 1
        
        return list;
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.length(headA)
        lenB = self.length(headB)
        
        list1, list2 = headA, headB
        
        if lenA > lenB:
            list1 = self.moveStep(headA, lenA - lenB)
            list2 = headB
        elif lenB > lenA:
            list1 = headA
            list2 = self.moveStep(headB, lenB - lenA)
            
        while list1 != list2:
            list1 = list1.next;
            list2 = list2.next;
            
        return list1
            
            
        
        
            