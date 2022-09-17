```
class Solution:
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
# Solution - Sorting + 2 Pointers
# Time - O(NlogN + M
# - N = len(products)
# - M = len(searchWord)
# Space - O(1)
products.sort()
n = len(products)
i, j = 0, n-1
result = []
for count, char in enumerate(searchWord):
while i < n and (count >= len(products[i]) or char != products[i][count]):
i += 1
​
while j > 0 and (count >= len(products[j]) or char != products[j][count]):
j -= 1
if i > j:
result.append([])
continue
result.append(products[i:min(j+1, i+3)])
return result
```
​
```
class Solution:
# Solution - Trie DFS
# Time - O(Nlog(N) + N*K)
# Space - O(26*N)
def traverse(self, trie, result):
if trie == None or len(result) == 3:
return
if self.end in trie:
result.append(trie[self.end])