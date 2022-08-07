```
class Solution:
MOD = (10 ** 9) + 7
@cache
def recur(self, cur, n):
if n == 0:
return 1
p = 0
for aj in ['a', 'e', 'i', 'o', 'u']:
if (cur, aj) in self.adjList:
p = (p + self.recur(aj, n-1) % self.MOD) % self.MOD
return p
def countVowelPermutation(self, n: int) -> int:
Solution - DP
Time - O(N*5)
Space - O(N*5)
self.adjList = {(-1, 'a'): 1, (-1, 'e'): 1, (-1, 'i'): 1, (-1, 'o'): 1, (-1, 'u'): 1, ('a', 'e'): 1, ('e', 'a'): 1, ('e', 'i'): 1, ('i', 'a'): 1, ('i', 'e'): 1, ('i', 'o'): 1, ('i', 'u'): 1, ('o', 'i'): 1, ('o', 'u'): 1, ('u', 'a'): 1}
return self.recur(-1, n)
```