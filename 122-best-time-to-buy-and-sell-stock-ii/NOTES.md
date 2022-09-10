```
class Solution0:
def maxProfit(self, prices: List[int]) -> int:
# Solution - Greedy - buy at valley and sell at peak
# Time - O(N)
# Space - O(1)
profit = 0
i = 0
while i < len(prices):
j = i
while j < len(prices)-1 and prices[j] < prices[j+1]:
j += 1
profit += (prices[j] - prices[i])
i = j + 1
return profit
```
```
class Solution:
def maxProfit(self, prices: List[int]) -> int:
# Solution - DP - iterative - Space Optimized
# Time - O(N*2)
#     - N = len(prices)
# Space - O(N*2)
n = len(prices)
pdp = [0] * 2
pdp[0] = pdp[1] = 0
for i in reversed(range(n)):
cdp = [0] * 2
for canBuy in range(2):
result = float('-inf')