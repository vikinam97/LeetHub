```
class Solution:
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
# Solution - using hash map
# Time - O(N)
# Space - O(N)
hashMap = [None]
node = head
while node:
hashMap.append(node)
nxt = node.next
node.next = None
node = nxt
heads = []
i = 0
while i + k < len(hashMap):
for j in range(i + k, i+1, -1):
hashMap[j].next = hashMap[j-1]
heads.append((hashMap[i+k], hashMap[i+1]))
i = i + k
if i + 1 < len(hashMap):
for j in range(i + 1, len(hashMap)-1):
hashMap[j].next = hashMap[j+1]
heads.append((hashMap[i+1], None))
for i in range(1, len(heads)):
heads[i-1][1].next = heads[i][0]
return heads[0][0]
```