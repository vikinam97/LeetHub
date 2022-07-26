#User function Template for python3


class Solution:
    def maxPalindrome(self,head):
        # Solution - reversing prev
        # Time - O(N*N)
        # Space - O(1)
        prev, next = None, None
        maxSoFar = 0
        
        while head:
            
            el = self.countCommon(head, prev)
            ol = self.countCommon(head.next, prev) + 1
            maxSoFar = max(maxSoFar, el, ol)
            
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        return maxSoFar
    
    def countCommon(self, l1, l2):
        count = 0
        while l1 and l2 and l1.data == l2.data:
            count += 1
            l1 = l1.next
            l2 = l2.next
        return 2 * count