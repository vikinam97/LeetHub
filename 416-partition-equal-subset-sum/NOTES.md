return False
target = int(target)
dp = [[False] * (target+1) for _ in range(len(nums))]
for i in range(len(nums)): dp[i][0] = True
if nums[0] <= target: dp[0][nums[0]] = True
for i in range(1, len(nums)):
for j in range(1, target+1):
dontTake = dp[i-1][j]
take = False
if nums[i] <= j:
take = dp[i-1][j - nums[i]]
dp[i][j] = take | dontTake
return dp[-1][-1]
​
```
```
class Solution:
def canPartition(self, nums: List[int]) -> bool:
# Solution - Recusion + Memoization
# Time - O(N * S)
#      - N = len(nums)
#      - S = sum(nums) / 2
# Space - O(N * S)
self.memo = {}
target = sum(nums)/2
if target != int(target):
return False
return self.recur(0, 0, int(target), nums)
def recur(self, idx, i, target, nums):
if idx >= len(nums):
return i == target
if i > target:
return False
if (idx, i) in self.memo:
return self.memo[(idx, i)]
self.memo[(idx, i)] = (self.recur(idx+1, i + nums[idx], target, nums) or
self.recur(idx+1, i, target, nums))
return self.memo[(idx, i)]
```