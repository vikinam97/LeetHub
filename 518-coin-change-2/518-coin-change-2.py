class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Solution - DP
        # Time - O(N*C)
        # Space - O(N)
        
        dp = [0] * (amount + 1)
        dp[0] = 1;
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] += dp[i - coin]
        return dp[-1];