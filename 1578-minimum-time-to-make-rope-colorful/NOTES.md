```
class Solution:
def minCost(self, colors: str, neededTime: List[int]) -> int:
# Solution - greedy - keep max in grp
# Time - O(N)
# Space - O(1)
cost = 0
i = 0
delCost = 0
while i < len(colors):
curColor = colors[i]
curSum, curMax = 0, float('-inf')
count = 0
while i < len(colors) and curColor == colors[i]:
curSum += neededTime[i]
curMax = max(curMax, neededTime[i])
count += 1
i += 1
if count > 1:
delCost += curSum - curMax
return delCost
```