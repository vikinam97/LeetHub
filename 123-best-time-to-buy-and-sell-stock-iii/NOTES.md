```
class Solution:
def maxProfit(self, prices: List[int]) -> int:
# Solution - DP - Iterative - Space Optimized
# Time - O(N*2*K)
#     - N = len(prices)
#     - k = 2
# Space - O(2*K)
n = len(prices)
pdp = [[0] * 3 for h in range(2)]
for i in reversed(range(n)):
cdp = [[0] * 3 for h in range(2)]
for canBuy in reversed(range(2)):
for k in reversed(range(1, 2+1)):
result = float('-inf')
if canBuy:
result = max(-prices[i] + pdp[0][k],
pdp[1][k])
else:
result = max(prices[i] + pdp[1][k-1],
pdp[0][k])
cdp[canBuy][k] = result