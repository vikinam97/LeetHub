MOD = (10**9) + 7
​
class Solution:
def numWays(self, steps: int, arrLen: int) -> int:
# Solution - Recursion + Memoization
# Time - O(K * N)
#     - K = steps
#     - N = arrLen
# Space - O(K*N)
self.memo = {}
return self.recur(0, arrLen, steps) % MOD
def recur(self, pos, n, k):
if pos >= n or pos < 0:
return 0
if k == 0:
return 1 if pos == 0 else 0
if pos > k:
return 0
if (pos, k) in self.memo:
return self.memo[(pos, k)]
self.memo[(pos, k)] = (self.recur(pos, n, k-1) +
self.recur(pos+1, n, k-1) +
self.recur(pos-1, n, k-1))
return self.memo[(pos, k)]