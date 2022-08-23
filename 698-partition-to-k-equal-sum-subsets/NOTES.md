```
class Solution:
def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
# Solution - Backtracking
# Time - O(O(K*2^N))
# Space - O(N)
if sum(nums) % k:
return False
nums.sort(reverse=True)
target = sum(nums) // k
used = [0] * len(nums)
def backtrack(i, curSum, k):
if k == 0:
return True
if curSum == target:
return backtrack(0, 0, k-1)
for j in range(i, len(nums)):
if used[j] or curSum + nums[j] > target or (j > 0 and nums[j] == nums[j-1] and not used[j-1]):
continue
used[j] = 1
if backtrack(j+1, curSum + nums[j], k):
return True
used[j] = 0
return backtrack(0, 0, k)
```