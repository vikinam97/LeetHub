class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution - buy at valley and sell at peak
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
            