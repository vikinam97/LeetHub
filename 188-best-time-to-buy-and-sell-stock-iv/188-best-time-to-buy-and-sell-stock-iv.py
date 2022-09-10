class Solution:
    def maxProfit(self, K, prices: List[int]) -> int:
        # Solution - DP - Iterative - Space Optimized
        # Time - O(N*2*K)
        #     - N = len(prices)
        #     - k = 2
        # Space - O(2*K)
        
        n = len(prices)
        pdp = [[0] * (K+1) for h in range(2)]
        
        for i in reversed(range(n)):
            cdp = [[0] * (K+1) for h in range(2)]
            for canBuy in reversed(range(2)):
                for k in reversed(range(1, (K+1))):
                    result = float('-inf')
        
                    if canBuy:
                        result = max(-prices[i] + pdp[0][k],
                                    pdp[1][k])
                    else:
                        result = max(prices[i] + pdp[1][k-1],
                                    pdp[0][k])
                    
                    cdp[canBuy][k] = result
            
            pdp = cdp
        
        return pdp[1][K]


class Solution1:
    def maxProfit(self, K, prices: List[int]) -> int:
        # Solution - DP - Iterative
        # Time - O(N*2*K)
        #     - N = len(prices)
        #     - k = 2
        # Space - O(N*2*K)
        
        n = len(prices)
        dp = [[[0] * (K+1) for h in range(2)] for _ in range(n + 1)]
        
        for i in reversed(range(n)):
            for canBuy in reversed(range(2)):
                for k in reversed(range(1, (K+1))):
                    result = float('-inf')
        
                    if canBuy:
                        result = max(-prices[i] + dp[i+1][0][k],
                                    dp[i+1][1][k])
                    else:
                        result = max(prices[i] + dp[i+1][1][k-1],
                                    dp[i+1][0][k])
                    
                    dp[i][canBuy][k] = result
        
        return dp[0][1][K]

class Solution2:
    def maxProfit(self, k, prices: List[int]) -> int:
        # Solution - Recursion + Memoization
        # Time - O(N*2*K)
        #     - N = len(prices)
        #     - k = 2
        # Space - O(N*2*K)
        
        self.memo = {}
        # 1 - BUY , 0 - SELL 
        return self.recur(0, 1, k, prices)
    
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