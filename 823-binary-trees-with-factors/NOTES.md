```
MOD = (10 ** 9) + 7
​
class Solution:
def numFactoredBinaryTrees(self, arr: List[int]) -> int:
# Solution - DP Iterative
# Time - O(N * N)
# Space - O(N)
dp = defaultdict(int)
hashSet = { i for i in arr}
arr.sort()
sm = 0
for i in arr:
dp[i] = 1
for j in arr:
if i / j in hashSet:
dp[i] = (dp[i] + (dp[j] * dp[i / j])) % MOD
sm = (sm + dp[i]) % MOD
return sm
```
```
class Solution:
def numFactoredBinaryTrees(self, arr: List[int]) -> int:
# Solution - recursion + memo
# Time - O(N * N)
# Space - O(N)
self.memo = {}
hashSet = { i for i in arr}
sm = 0
for i in arr:
rsm = self.recur(i, arr, hashSet)
sm = (sm + (rsm + 1)) % MOD
return sm
def recur(self, parent, arr, hashSet):
if parent in self.memo:
return self.memo[parent]
sm = 0
for i in arr:
if (parent / i) in hashSet:
sm = ( sm +
((self.recur(i, arr, hashSet) + 1) % MOD) *
((self.recur(parent / i, arr, hashSet) + 1) % MOD)) % MOD
self.memo[parent] = sm
return sm
```