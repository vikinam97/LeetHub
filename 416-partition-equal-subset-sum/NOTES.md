```
class Solution:
def canPartition(self, nums: List[int]) -> bool:
# Solution - DP
# Time - O(N * S)
#      - N = len(nums)
#      - S = sum(nums) / 2
# Space - O(N * S)
target = sum(nums)/2
if target != int(target):
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