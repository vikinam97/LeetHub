
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution - Recursion + Memoization
        # Time - O(N*2)
        #     - N = len(prices)
        # Space - O(N*2)
        
        self.memo = {}
        # 1 - BUY , 0 - SELL 
        return self.recur(0, 1, prices)
    
    def recur(self, i, canBuy, prices):
        if i >= len(prices):
            return 0
        
        if (i, canBuy) in self.memo:
            return self.memo[(i, canBuy)]
        
        result = float('-inf')
        
        if canBuy:
            result = max(-prices[i] + self.recur(i+1, 0, prices),
                        self.recur(i+1, 1, prices))
        else:
            result = max(prices[i] + self.recur(i+2, 1, prices),
                        self.recur(i+1, 0, prices))
            
        self.memo[(i, canBuy)] = result
        return result
            