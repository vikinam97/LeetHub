```
class Solution:
def decode(self, encoded: List[int], first: int) -> List[int]:
# Time -> O(n)
# Space -> O(n) for the result array
resultList = [0] * (len(encoded) + 1)
resultList[0] = first
for i in range(1, len(resultList)):
resultList[i] = resultList[i-1] ^ encoded[i-1]
return resultList
```