```
class Solution:
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
# Solution - Longest common sub string - space optimised
# Time - O(N*M)
# Space - O(M)
pdp = [0] * (len(nums2)+1)
maxSoFar = 0
for i in range(1, len(nums1)+1):
cdp = [0] * (len(nums2)+1)
for j in range(1, len(nums2)+1):
if nums1[i-1] == nums2[j-1]:
cdp[j] = pdp[j-1] + 1
maxSoFar = max(maxSoFar, cdp[j])
pdp = cdp
return maxSoFar
​
```
```
​
class Solution1:
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
# Solution - Longest common sub string
# Time - O(N*M)
# Space - O(N*M)
dp = [[0] * (len(nums2)+1) for _ in range(len(nums1) + 1)]
maxSoFar = 0
for i in range(1, len(nums1)+1):
for j in range(1, len(nums2)+1):
if nums1[i-1] == nums2[j-1]:
dp[i][j] = dp[i-1][j-1] + 1
maxSoFar = max(maxSoFar, dp[i][j])
​
return maxSoFar
```