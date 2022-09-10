```
class Solution:
def maxProfit(self, prices: List[int]) -> int:
# Solution - Recursion + Memoization
# Time - O(N*2*K)
#     - N = len(prices)
#     - k = 2
# Space - O(N*2*K)
self.memo = {}
# 1 - BUY , 0 - SELL
return self.recur(0, 1, 2, prices)
def recur(self, i, canBuy, k, prices):
if i >= len(prices) or k <= 0:
return 0
if (i, k, canBuy) in self.memo:
return self.memo[(i, k, canBuy)]
result = float('-inf')
if canBuy:
result = max(-prices[i] + self.recur(i+1, 0, k, prices),
self.recur(i+1, 1, k, prices))
else:
result = max(prices[i] + self.recur(i+1, 1, k-1, prices),
self.recur(i+1, 0, k, prices))
self.memo[(i, k, canBuy)] = result
return result
```