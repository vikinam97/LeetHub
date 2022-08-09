```
class Solution:
def partitionLabels(self, s: str) -> List[int]:
# Solution - Greedy
# Time - O(N)
#     - N -> length of string
# Space - O(N)
lastSeen = defaultdict(int)
for i in range(len(s)):
lastSeen[s[i]] = i
i, j = 0, 0
seenChar = set()
result = []
while i < len(s):
seenChar.add(s[i])
possiblePartition = True
for char in seenChar:
if lastSeen[char] > i:
possiblePartition = False
i += 1
if possiblePartition:
seenChar = set()
result.append(i - j)
j = i
return result
```