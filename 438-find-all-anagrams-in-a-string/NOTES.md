```
class Solution:
def findAnagrams(self, s: str, p: str) -> List[int]:
# Solution - Sliding Window
# Time - O(N)
# Space - O(N)
reqChar, reqCharCount = defaultdict(int), 0
for char in p:
reqChar[char] += 1
reqCharCount = len(reqChar.keys())
seenChar = defaultdict(int)
seenCharCount = 0
reqSeenCharCount = 0
j = 0
result = []
for idx, char in enumerate(s):
if seenChar[char] == 0:
seenCharCount += 1
seenChar[char] += 1
if char in reqChar and reqChar[char] == seenChar[char]:
reqSeenCharCount += 1
while reqSeenCharCount == reqCharCount:
if reqCharCount == seenCharCount and (idx - j + 1) == len(p):
result.append(j)
seenChar[s[j]] -= 1
if seenChar[s[j]] == 0:
seenCharCount -= 1
if s[j] in reqChar and seenChar[s[j]] < reqChar[s[j]]:
reqSeenCharCount -= 1
j += 1
return result
```