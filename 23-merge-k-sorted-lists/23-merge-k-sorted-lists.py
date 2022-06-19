# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        
        minHeap = []
        
        # init all nodes to minHeap
        for head in lists:
            if head:
                heapq.heappush(minHeap, head)
        
        newHead = None
        head = None 

        while minHeap:
            node = heapq.heappop(minHeap)
            if newHead == None:
                newHead = node
                head = node
            else:
                newHead.next = node
                newHead = newHead.next
            if node.next:
                heapq.heappush(minHeap, node.next)
        
        return head