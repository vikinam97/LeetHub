```
class Solution:
def isUniversal(self, word, rHash):
wHash = [0] * 26
for char in word:
wHash[ord(char) - ord('a')] += 1
for i in range(26):
if rHash[i] > wHash[i]:
return False
return True
def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
# Solution - Hash Table
# Time - O(N * M * 26)
# Space - O(26)
reqHash = [0] * 26
for word in words2:
wHash = [0] * 26
for char in word:
key = ord(char) - ord('a')
wHash[key] += 1
reqHash[key] = max(wHash[key], reqHash[key])
result = []
for word in words1:
if self.isUniversal(word, reqHash):
result.append(word)
return result
```