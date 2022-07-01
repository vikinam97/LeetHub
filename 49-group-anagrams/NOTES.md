```
class Solution:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# Solution - sorted key hash
# Time - (N * MlogM)
#     - N = numbers of strings
#     - M = length of longest string
# Space - O(N)
grpSet = defaultdict(list)
for i in range(len(strs)):
key = sorted(strs[i])
key = "".join(key)
grpSet[key].append(strs[i])
return grpSet.values()
```