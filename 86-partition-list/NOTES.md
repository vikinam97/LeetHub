```
class Solution:
def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
# Solution - seperation
# Time - O(N)
# Space - O(1)
lHead = ListNode("/")
gHead = ListNode('/')
temp = head
lNode = lHead
gNode = gHead
while temp:
if temp.val < x:
lNode.next = temp
lNode = lNode.next
else:
gNode.next = temp
gNode = gNode.next
temp = temp.next
lNode.next = gHead.next
gNode.next = None
return lHead.next
```