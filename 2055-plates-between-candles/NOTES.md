```
class Solution:
def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
# Solution - Binary serach + REfix sum of candles
# Time - O(N + QlogN)
#     - N = len(s)
#     - Q = len(queries)
# Space - O(N)
starSum, barIdxs = [0]*len(s), []
for i in range(len(s)):
if s[i] == '|':
barIdxs.append(i)
starSum[i] = starSum[i-1]
else:
starSum[i] = starSum[i-1] + 1
result = []
​
for s, e in queries:
sb = bisect.bisect_left(barIdxs, s)
eb = bisect.bisect_right(barIdxs, e)
if sb == eb:
result.append(0)
continue
startStarSum = starSum[barIdxs[sb]]
lastStarSum = starSum[barIdxs[eb-1]]
​
result.append(lastStarSum - startStarSum)
return result
```