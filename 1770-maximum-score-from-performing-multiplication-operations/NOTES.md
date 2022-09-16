```
class Solution:
def maximumScore(self, nums: List[int], muls: List[int]) -> int:
# Solution - DP - Space Optimized
# Time - O(M*M)
# Space - O(M)
n, m = len(nums), len(muls)
pdp = [0]*(m+1)
for i in range(m - 1, -1, -1):
cdp = [0]*(m+1)
for s in range(i, -1, -1):
cdp[s] = max(
(muls[i]*nums[s]) + pdp[s+1],
(muls[i]*nums[n - 1 - (i - s)]) + pdp[s])
pdp = cdp
return pdp[0]
```
```
​
class Solution:
def maximumScore(self, nums: List[int], muls: List[int]) -> int:
# Solution - Iterative DP
# Time - O(M*M)
# Space - O(M*M)
n, m = len(nums), len(muls)
dp = [[0]*(m+1) for _ in range(m+1)]
for i in range(m - 1, -1, -1):
for s in range(i, -1, -1):
dp[i][s] = max(
(muls[i]*nums[s]) + dp[i+1][s+1],
(muls[i]*nums[n - 1 - (i - s)]) + dp[i+1][s])
return dp[0][0]
```
```
​