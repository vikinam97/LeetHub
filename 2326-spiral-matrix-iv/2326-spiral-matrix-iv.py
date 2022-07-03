# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Solution - traversal
        # Time - O(N)
        # Space - O(N)
        top, bottom = 0, m
        left, right = 0, n
        
        matrix = []
        for i in range(m):
            matrix.append([-1] * n)
            
        while top < bottom:
            # traverse top
            for i in range(left, right):
                if head == None: break;
                matrix[top][i] = head.val
                head = head.next
            top += 1
            # traverse right
            for i in range(top, bottom):
                if head == None: break;
                matrix[i][right-1] = head.val
                head = head.next
            bottom -= 1
            
            # traverse bottom
            i = right - 2
            while i >= left:
                if head == None: break;
                matrix[bottom][i] = head.val
                head = head.next
                i -= 1 
            right -= 1
            
            # traverse left
            i = bottom - 1
            while i >= top:
                if head == None: break;
                matrix[i][left] = head.val
                head = head.next
                i -= 1
            left += 1
        
        return matrix
            
            
            
            
            
            
            
            
            