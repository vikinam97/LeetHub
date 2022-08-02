```
class CombinationIterator:
def backtrack(self, i, charSet, k, path):
if i == k:
self.combos.append("".join(path))
return
for idx, key in enumerate(charSet):
path.append(key)
self.backtrack(i + 1, charSet[idx+1:], k, path)
path.pop()
​
def __init__(self, characters: str, combinationLength: int):
self.combos = deque([])
self.backtrack(0, characters, combinationLength, [])
​
def next(self) -> str:
if len(self.combos):
return self.combos.popleft()
​
def hasNext(self) -> bool:
return len(self.combos) != 0
```