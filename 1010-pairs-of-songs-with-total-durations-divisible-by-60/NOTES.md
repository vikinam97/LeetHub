```
class Solution:
def numPairsDivisibleBy60(self, time: List[int]) -> int:
# Solution - 2 Sum  - 60 - n%60 in seen or not
# Time - O(N)
# Space - O(N)
hashMap = defaultdict(int)
count = 0
for num in time:
key = 60 - (num%60)
if key in hashMap:
count += hashMap[key]
elif key == 60:
count += hashMap[0]
hashMap[num%60] += 1
return count
```