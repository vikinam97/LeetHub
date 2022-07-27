```
class Solution:
def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
# Solution - trversal DFS
# Time - O(N)
# Space - O(N)
if not head:
return  head
self.current = Node("/", None, None, None)
self.recur(head)
head.prev = None
return head
def recur(self, levelHead):
if not levelHead:
return
temp = levelHead
while temp:
self.current.next = temp
temp.prev = self.current
self.current = self.current.next
next = temp.next
child = temp.child
temp.child = None
if child:
self.recur(child)
temp = next
```
​