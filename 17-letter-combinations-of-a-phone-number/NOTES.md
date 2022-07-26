```
class Solution:
digiMap = [
[],
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l'],
['m', 'n', 'o'],
['p', 'q', 'r', 's'],
['t', 'u', 'v'],
['w', 'x', 'y', 'z'],
]
def letterCombinations(self, digits: str) -> List[str]:
# Solution - backtrack - permute
# Time - O(3^N)
#     N - no of digits
# Space - O(3^N)
self.combo = []
self.recur(0, digits, [])
return self.combo
def recur(self, i, digits, path):
if i >= len(digits):
if len(path):