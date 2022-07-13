```
class Solution:
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Solution - fast and slow pointer
# Time - O(N)
# Space - O(1)
# first check cycle or not
slow, fast = head, head
while fast and fast.next:
slow = slow.next
fast = fast.next.next
if slow == fast:
break
if not fast or not fast.next:
return None
# if cycle -> slow and fast meet at mid of the list
# fast dist from point od cycle
#  = slow dist from point of cycle
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
```