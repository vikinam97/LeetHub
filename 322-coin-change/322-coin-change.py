class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Solution - Dynamic programming - Tabulation
        # Time - O(N)
        # Space - O(N)
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
        