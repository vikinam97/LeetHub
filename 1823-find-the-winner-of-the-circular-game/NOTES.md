```
class Node:
def __init__(self, val, next=None):
self.val = val
self.next = next
class Solution:
def findTheWinner(self, n: int, k: int) -> int:
# Solution - Linked list simulation
# Time - O(N * K)
# Space - O(N)
head = Node("/")
temp = head
for i in range(1, n+1):
temp.next = Node(i)
temp = temp.next
temp.next = head.next
prev = temp
temp = head.next
head = temp
count = 0
while count < n:
for i in range(1, k):
prev = temp
temp = temp.next
prev.next = temp.next
temp = prev.next
count += 1
​
return temp.val
```