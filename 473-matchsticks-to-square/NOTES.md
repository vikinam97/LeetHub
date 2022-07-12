```
class Solution:
def makesquare(self, matchsticks: List[int]) -> bool:
# Solution - backtracking + memo
# Time - O(N^4)
# Space - O(N)
sm = sum(matchsticks)
if sm < 4:
return False
if sm % 4 != 0:
return False
k = sm // 4
memo = {}
matchsticks.sort(reverse=True)
@cache
def recur(cur, s1, s2, s3, s4):
if cur >= len(matchsticks):
return  s1 == k and s2 == k and s3 == k and s4 == k
if s1 > k or s2 > k or s3 > k or s4 > k:
return False
return (recur(cur+1, s1 + matchsticks[cur], s2, s3, s4) or
recur(cur+1, s1, s2 + matchsticks[cur], s3, s4) or
recur(cur+1, s1, s2, s3 + matchsticks[cur], s4) or
recur(cur+1, s1, s2, s3, s4 + matchsticks[cur]))
return recur(0, 0,0,0,0)
```